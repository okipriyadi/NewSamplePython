#!/usr/bin/env python

########################################################################################################################
# IMPORTS
########################################################################################################################
from sys import stdout
from subprocess import check_output, STDOUT
from traceback import format_exc
from argparse import ArgumentParser
from twisted.internet.base import DelayedCall
from twisted.internet import reactor
from twisted.internet.protocol import Factory, ClientFactory, ReconnectingClientFactory
from twisted.python import log
from twisted.protocols.basic import LineOnlyReceiver
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol, JSONRPCRequest, JSONRPCSuccessResponse, JSONRPCErrorResponse
from twisted.python.failure import Failure
from tinyrpc.exc import RPCError, MethodNotFoundError


########################################################################################################################
# CONSTANTS
########################################################################################################################
MOUNT_ENABLED                    = True
IFE_API_IPC_PROXY_LISTENING_PORT = 8888
IFE_PROXY_TIMEOUT                = 5
IFE_IPC_PORT_SIM                 = str('%d,%d' % (50004, 50005))
IFE_IPC_HOST_SIM                 = '127.0.0.1'
TRANSFER_EVENT_TIMEOUT           = 120

########################################################################################################################
# CLASSES
########################################################################################################################
class IFEIPCProxyCommonProtocol(LineOnlyReceiver):
    def __init__(self, command, value):
        assert isinstance(command, (str, unicode))
        assert isinstance(value, (int, long))
        self.command = command
        self.value = value
        self.rpc = JSONRPCProtocol()
        self.cmd_handler = {'wifi'   : self.cmd_wifi,
                            'lte'    : self.cmd_lte,
                            'wap'    : self.cmd_wap}
        
    def connectionMade(self):
        try:
            handler = self.cmd_handler[self.command]
            assert callable(handler)
            handler()
        except Exception:
            self.transport.loseConnection()        
    
    def connectionLost(self, reason):
        assert isinstance(reason, Failure)
        log.msg('ife-api-ipc-proxy endpoint closed')
    
    def lineReceived(self, line):
        assert isinstance(line, (str, unicode))                
    
    def cmd_wifi(self):
        kwargs = {'Type' : 'WIFI_STATUS',
                  'Status' : int(self.value)}
        event = self.rpc.create_request('system-event', kwargs = kwargs, one_way=True)        
        self.sendLine(event.serialize())
        reactor.callLater(0.1, self.transport.loseConnection) #@UndefinedVariable
    
    def cmd_lte(self):
        kwargs = {'Type' : 'LTE_STATUS',
                  'Status' : int(self.value)}
        event = self.rpc.create_request('system-event', kwargs = kwargs, one_way=True)
        self.sendLine(event.serialize())
        reactor.callLater(0.1, self.transport.loseConnection) #@UndefinedVariable
        
    def cmd_wap(self):
        kwargs = {'Type' : 'WAP_STATUS',
                  'Status' : int(self.value)}
        event = self.rpc.create_request('system-event', kwargs = kwargs, one_way=True)
        self.sendLine(event.serialize())
        reactor.callLater(0.1, self.transport.loseConnection) #@UndefinedVariable
        
class IFEIPCProxyCommonFactory(ClientFactory):
    noisy = False
    def __init__(self, command, value):
        assert isinstance(command, (str, unicode))
        assert isinstance(value, (int, long))
        self.command = command
        self.value = value
    
    def buildProtocol(self, addr):
        return IFEIPCProxyCommonProtocol(self.command, self.value)
    
class IFEIPCProxyServerProtocol(LineOnlyReceiver):
    def __init__(self, clients, transports, ipc_host, ipc_port_common, ipc_port_sync):
        assert isinstance(clients, dict)
        assert isinstance(transports, dict)
        assert isinstance(ipc_host, (str, unicode))
        assert isinstance(ipc_port_common, (int, long))
        assert isinstance(ipc_port_sync, (int, long))
        self.clients = clients        
        self.transports = transports        
        self.ipc_host = ipc_host
        self.ipc_port_common = ipc_port_common
        self.ipc_port_sync = ipc_port_sync
        self.rpc = JSONRPCProtocol()
        self.client_id = None
        self.path_mounted = None
        self.methods = {'ife-ipc-proxy-mount'   : self.ife_ipc_proxy_mount,
                        'ife-ipc-proxy-unmount' : self.ife_ipc_proxy_unmount,
                        'ife-ipc-proxy-wifi'    : self.ife_ipc_proxy_wifi,
                        'ife-ipc-proxy-lte'     : self.ife_ipc_proxy_lte,
                        'ife-ipc-proxy-wap'     : self.ife_ipc_proxy_wap,}
    
    def connectionMade(self):
        pass
    
    def connectionLost(self, reason):
        assert isinstance(reason, Failure)           
        if self.client_id != None:
            self.clients.pop(self.client_id, None)
    
    def lineReceived(self, line):
        assert isinstance(line, (str, unicode))
        try:
            request = self.rpc.parse_request(line)
            self.requestReceived(request)
        except RPCError:
            try:
                response = self.rpc.parse_reply(line)
                self.responseReceived(response)
            except RPCError:
                peer = self.transport.getPeer()
                log.msg('failed to parse message from %s:%d, message = %s' % (peer.host, peer.port, line))
            except Exception:
                log.msg('failed to parse response, %s' % format_exc())                    
        except Exception:
            log.msg('failed to parse request, %s' % format_exc())
    
    def requestReceived(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            handler = self.methods[request.method]
            assert callable(handler)
            handler(request)
        except KeyError as e:
            log.msg('no such RPC method %s' % e.message)
            error = MethodNotFoundError(request.method)
            response = request.error_respond(error)
            if response:
                self.sendLine(response.serialize())
        except AssertionError:
            log.msg('RPC method %s is not callable' % request.method)
            response = request.error_respond('RPC not callable')
            if response:
                self.sendLine(response.serialize())
        except Exception:
            log.msg('failed to process RPC request, %s' % format_exc()) 
    
    def responseReceived(self, response):
        assert isinstance(response, (JSONRPCSuccessResponse, JSONRPCErrorResponse))
    
    def ife_ipc_proxy_mount(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            client_id = request.kwargs['id']
            assert isinstance(client_id, (int, long)), 'client_id'
            if client_id not in self.clients:
                self.clients[client_id] = self.transport
                self.client_id = client_id                        
                self.ipc_forward('mount', client_id, request.unique_id)
            else:
                self.transport.loseConnection()
        except KeyError as e:
            log.msg('missing parameter %s from ife-ipc-proxy-mount command' % e.message)
        except AssertionError:
            log.msg('bad parameter type %s from ife-ipc-proxy-mount command' % e.message)
        except Exception:
            log.msg('failed to process ife-ipc-proxy-mount, %s' % format_exc())            
    
    def ife_ipc_proxy_unmount(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            client_id = request.kwargs['id']
            assert isinstance(client_id, (int, long)), 'client_id'
            if client_id not in self.clients:
                self.clients[client_id] = self.transport
                self.client_id = client_id                        
                self.ipc_forward('unmount', client_id, request.unique_id)
            else:
                self.transport.loseConnection()
        except KeyError as e:
            log.msg('missing parameter %s from ife-ipc-proxy-unmount command' % e.message)
        except AssertionError:
            log.msg('bad parameter type %s from ife-ipc-proxy-unmount command' % e.message)
        except Exception:
            log.msg('failed to process ife-ipc-proxy-unmount, %s' % format_exc())     
    
    def ife_ipc_proxy_wifi(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            status = request.kwargs['status']
            assert isinstance(status, (int, long)), 'status'
            value = 1 if status > 0 else 0
            self.ipc_forward('wifi', value, request.unique_id)
        except KeyError as e:
            log.msg('missing parameter %s from ife-ipc-proxy-wifi command' % e.message)
        except AssertionError:
            log.msg('bad parameter type %s from ife-ipc-proxy-wifi command' % e.message)
        except Exception:
            log.msg('failed to process ife-ipc-proxy-wifi, %s' % format_exc())     
    
    def ife_ipc_proxy_lte(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            status = request.kwargs['status']
            assert isinstance(status, (int, long)), 'status'
            value = 1 if status > 0 else 0
            self.ipc_forward('lte', value, request.unique_id)
        except KeyError as e:
            log.msg('missing parameter %s from ife-ipc-proxy-lte command' % e.message)
        except AssertionError:
            log.msg('bad parameter type %s from ife-ipc-proxy-lte command' % e.message)
        except Exception:
            log.msg('failed to process ife-ipc-proxy-lte, %s' % format_exc())    
    
    def ife_ipc_proxy_wap(self, request):
        assert isinstance(request, JSONRPCRequest)
        
        try:
            status = request.kwargs['status']
            assert isinstance(status, (int, long)), 'status'
            value = 1 if status > 0 else 0
            self.ipc_forward('wap', value, request.unique_id)
        except KeyError as e:
            log.msg('missing parameter %s from ife-ipc-proxy-wap command' % e.message)
        except AssertionError:
            log.msg('bad parameter type %s from ife-ipc-proxy-wap command' % e.message)
        except Exception:
            log.msg('failed to process ife-ipc-proxy-wap, %s' % format_exc())
    
    def ipc_forward(self, command, value, unique_id = None):
        assert isinstance(command, (str, unicode))
        assert isinstance(value, (int, long))
        
        if command in ('mount', 'unmount'):
            proto = self.transports.get('sync', None)
            if proto:
                handler = getattr(proto, command)
                if callable(handler):
                    handler('/media/usb1', value, unique_id)
                else:
                    log.msg('sync connection does not have method %s' % command)
            else:
                log.msg('sync connection to ife-api is down')
        elif command in ('wifi', 'lte' ):
            reactor.connectTCP(self.ipc_host, self.ipc_port_sync, IFEIPCProxyCommonFactory(command, value)) #@UndefinedVariable
            
        else:
            reactor.connectTCP(self.ipc_host, self.ipc_port_common, IFEIPCProxyCommonFactory(command, value)) #@UndefinedVariable
        
        
class IFEIPCProxyServerFactory(Factory):
    noisy = False
    def __init__(self, clients, transports, ipc_host, ipc_port_common, ipc_port_sync):
        assert isinstance(clients, dict)
        assert isinstance(transports, dict)
        assert isinstance(ipc_host, (str, unicode))
        assert isinstance(ipc_port_common, (int, long))
    assert isinstance(ipc_port_sync, (int, long))
        self.clients = clients
        self.transports = transports
        self.ipc_host = ipc_host
        self.ipc_port_common = ipc_port_common
    self.ipc_port_sync = ipc_port_sync
    
    def buildProtocol(self, addr):
        return IFEIPCProxyServerProtocol(self.clients, self.transports, self.ipc_host, self.ipc_port_common, self.ipc_port_sync )

class IFEIPCProxySyncProtocol(LineOnlyReceiver):
    def __init__(self, clients, transports, watchdogs):
        assert isinstance(clients, dict)
        assert isinstance(transports, dict)
        assert isinstance(watchdogs, dict)
        self.clients = clients
        self.transports = transports
        self.watchdogs = watchdogs
        self.rpc = JSONRPCProtocol()
        self.methods = {'transfer-event' : self.transferEventReceived}
    
    def connectionMade(self):
        self.transports['sync'] = self
    
    def connectionLost(self, reason):
        assert isinstance(reason, Failure)
        self.transports.pop('sync', None)
    
    def lineReceived(self, line):
        assert isinstance(line, (str, unicode))
        try:
            request = self.rpc.parse_request(line)
            self.requestReceived(request)
        except RPCError:
            try:
                response = self.rpc.parse_reply(line)
                self.responseReceived(response)
            except RPCError:
                peer = self.transport.getPeer()
                log.msg('failed to parse message from %s:%d, message = %s' % (peer.host, peer.port, line))
            except Exception:
                log.msg('failed to parse response, %s' % format_exc())                    
        except Exception:
            log.msg('failed to parse request, %s' % format_exc())
    
    def requestReceived(self, request):
        assert isinstance(request, JSONRPCRequest)
        try:
            handler = self.methods[request.method]
            assert callable(handler)
            handler(request)
        except KeyError as e:
            log.msg('no such RPC method %s' % e.message)
            error = MethodNotFoundError(request.method)
            response = request.error_respond(error)
            if response:
                self.sendLine(response.serialize())
        except AssertionError:
            log.msg('RPC method %s is not callable' % request.method)
            response = request.error_respond('RPC not callable')
            if response:
                self.sendLine(response.serialize())
        except Exception:
            log.msg('failed to process RPC request, %s' % format_exc()) 
    
    def responseReceived(self, response):
        assert isinstance(response, (JSONRPCSuccessResponse, JSONRPCErrorResponse))
        
    def mount(self, mount_point, client_id, unique_id = None):
        assert isinstance(mount_point, (str, unicode))
        assert isinstance(client_id, (int, long))
        
        if MOUNT_ENABLED:
            mount_dst = str('/vm/vps/root/%d/media/usb1' % client_id)
            mount_src = '/store1/usb'
            command = str('ssh root@10.0.200.1 mount -n -t simfs %s %s -o %s' % (mount_src, mount_dst, mount_src))
            try:
                check_output(command, stderr=STDOUT, shell=True)
            except Exception as e:
                log.msg('failed to mount vps drive, %s' % e.message)
                
        kwargs = {'Type' : 'MOUNT_STATUS',
                  'Mount_point' : mount_point,
                  'id' : client_id}
        request = self.rpc.create_request('system-event', kwargs = kwargs)
        request.unique_id = unique_id
        self.sendLine(request.serialize()) 
        watchdog = self.watchdogs.pop(client_id, None)
        if isinstance(watchdog, DelayedCall) and (not watchdog.cancelled) and (not watchdog.called):
            watchdog.cancel()
        self.watchdogs[client_id] = reactor.callLater(TRANSFER_EVENT_TIMEOUT, self.watchdog, client_id) #@UndefinedVariable       
    
    def unmount(self, mount_point, client_id, unique_id = None):
        assert isinstance(mount_point, (str, unicode))
        assert isinstance(client_id, (int, long))
                
        kwargs = {'Type' : 'UNMOUNT_STATUS',
                  'Mount_point' : mount_point,
                  'id' : client_id}
        event = self.rpc.create_request('system-event', kwargs = kwargs, one_way=True)
        self.sendLine(event.serialize())
        watchdog = self.watchdogs.pop(client_id, None)
        if isinstance(watchdog, DelayedCall) and (not watchdog.cancelled) and (not watchdog.called):
            watchdog.cancel()
        
        if MOUNT_ENABLED:
            path_mounted = str('/vm/vps/root/%d/media/usb1' % client_id)
            command = str('ssh root@10.0.200.1 umount %s' % path_mounted)
            while True:
                try:
                    check_output(command, stderr=STDOUT, shell=True)
                except Exception:
                    break
    
    def transferEventReceived(self, request):
        try:
            status = request.kwargs['Status']
            client_id = request.kwargs['id'] 
            assert isinstance(status, (int, long))
            assert isinstance(client_id, (int, long))
        except KeyError as e:
            log.msg('missing parameter %s' % e.message)
        except AssertionError:
            log.msg('bad parameter type')
        else:
            transport = self.clients.get(client_id, None)
            if transport:
                transport.writeSequence((request.serialize(), self.delimiter))
                
            if status == 0:
                log.msg('transfer to client %d progressing' % client_id)
                watchdog = self.watchdogs.get(client_id, None)
                if isinstance(watchdog, DelayedCall) and (not watchdog.cancelled) and (not watchdog.called):
                    watchdog.reset(TRANSFER_EVENT_TIMEOUT)                        
            elif status == 1:
                log.msg('transfer to client %d failed' % client_id)
                self.unmount('/media/usb1', client_id)
            elif status == 2:
                log.msg('transfer to client %d finished' % client_id)
                self.unmount('/media/usb1', client_id)
            else:
                log.msg('unknown transfer status %d from client id %d' % (status, client_id))
                self.unmount('/media/usb1', client_id)
    
    def watchdog(self, client_id):
        assert isinstance(client_id, (int, long))
        log.msg('no transfer-event after %d seconds, dismounting' % TRANSFER_EVENT_TIMEOUT)
        self.unmount('/media/usb1', client_id)

class IFEIPCProxySyncFactory(ReconnectingClientFactory):
    maxDelay = 1
    noisy = False

    def __init__(self, clients, transports):
        assert isinstance(clients, dict)
        assert isinstance(transports, dict)
        self.clients = clients
        self.transports = transports
        self.watchdogs = {}
    
    def buildProtocol(self, addr):
        self.resetDelay()
        return IFEIPCProxySyncProtocol(self.clients, self.transports, self.watchdogs)

    def clientConnectionLost(self, connector, reason):
        assert isinstance(reason, Failure)
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        assert isinstance(reason, Failure)
        ReconnectingClientFactory.clientConnectionFailed(self, connector, reason)
    
class IFEIPCProxyServer(object):
    def __init__(self, listen, host, ports):
        assert isinstance(listen, (int, long))
        assert isinstance(ports, (str, unicode))
        self.clients = {}
        self.transports = {}
        self.host = host or IFE_IPC_HOST_SIM
        self.ports = ports or IFE_IPC_PORT_SIM
        self.listen = listen or IFE_API_IPC_PROXY_LISTENING_PORT
    
    def run(self):
        port_sync, port_common = self.ports.split(',')
        port_sync, port_common = int(port_sync), int(port_common)
        reactor.connectTCP(self.host, port_sync, IFEIPCProxySyncFactory(self.clients, self.transports)) #@UndefinedVariables
        reactor.listenTCP(self.listen, IFEIPCProxyServerFactory(self.clients, self.transports, self.host, port_common, port_sync)) #@UndefinedVariable
        reactor.run() #@UndefinedVariable

########################################################################################################################
# METHODS
########################################################################################################################
def init_parser():
    parser = ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='0.0.1')    
    parser.add_argument('-l', '--listen', help="IFE API proxy listening port", type=int, default=IFE_API_IPC_PROXY_LISTENING_PORT)
    parser.add_argument('-s', '--server', help="IP address of IFE-API IPC server", type=str, default=IFE_IPC_HOST_SIM)
    parser.add_argument('-p', '--ports', help="Port pair of IFE-API IPC server (format=port1,port2)", type=str, default=IFE_IPC_PORT_SIM)    
    return parser
        
def main():
    try:
        log.startLogging(stdout)
        parser = init_parser()
        args = parser.parse_args()
        IFEIPCProxyServer(args.listen, args.server, args.ports).run()
    except Exception:
        log.msg('IFE system client simulator failure, %s' % format_exc())        

if __name__ == '__main__':
    main()