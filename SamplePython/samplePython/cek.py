from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineOnlyReceiver
from tinyrpc.protocols.jsonrpc import JSONRPCProtocol, JSONRPCRequest, JSONRPCSuccessResponse, JSONRPCErrorResponse

#class Echo(protocol.Protocol):#our own Echo protocol by subclassing protocol.Protocol

class Echo(LineOnlyReceiver):#our own Echo protocol by subclassing protocol.Protocol
    rpc = JSONRPCProtocol()
    def dataReceived(self, data): #dataReceived : Called when data is received across a transport.
        print "data = ", repr(data)
        data = data.replace("\r", "")
        print "data after replace = ", repr(data)
        delimiter = b'\n'
        lines  = (self._buffer+data).split(delimiter)
        
        print "lines =", lines
        
        self._buffer = lines.pop(-1)
        print "self._buffer =", repr(self._buffer) 
        for line in lines:
            if self.transport.disconnecting:
                # this is necessary because the transport may be told to lose
                # the connection by a line within a larger packet, and it is
                # important to disregard all the lines in that packet following
                # the one that told it to close.
                return
            if len(line) > self.MAX_LENGTH:
                return self.lineLengthExceeded(line)
            else:
                self.lineReceived(line)
        if len(self._buffer) > self.MAX_LENGTH:
            return self.lineLengthExceeded(self._buffer)
      
    def lineReceived(self, line):
        print "data lineRec=", repr(line), "finished"
        try:
            rpc = JSONRPCProtocol
            request = self.rpc.parse_request(line)
            print "request =",request
            
            #self.requestReceived(request)
        except RPCError:
            pass
        """
            try:
                response = self.rpc.parse_reply(line)
                self.responseReceived(response)
            except RPCError:
                self.transport.loseConnection()
                peer = self.transport.getPeer()
                log.msg('failed to parse message from %s:%d, message = %s' % (peer.host, peer.port, line), syslogPriority=WARNING)
            except Exception:
                self.transport.loseConnection()
                log.msg('failed to parse response, %s' % format_exc(), syslogPriority=CRITICAL)                    
        except Exception:
            self.transport.loseConnection()
            log.msg('failed to parse request, %s' % format_exc(), syslogPriority=CRITICAL)
            """ 
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):#method_to_buildprotocol, when connection from client made this function start
        print "addr =", addr
        return Echo()
print "reactor start"
reactor.listenTCP(8000, EchoFactory())
reactor.run()