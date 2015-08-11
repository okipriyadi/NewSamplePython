from tinyrpc.protocols.jsonrpc import JSONRPCProtocol
import socket

def provision_wap_conf():
    request = JSONRPCProtocol().create_request('wap_conf')
    data = request.serialize()
    result = send_request('localhost', 5050, data, wait_for_eof = True)
    return result

def send_request(dest, port, request, wait_for_eof = False):
    status_msg = ""

    try:
        sock = socket.create_connection((dest, port), timeout=10)
    except Exception, error:
        return {'error': 'Connection Error: ' + str(error)}, status_msg

    try:
        sock.sendall(request + '\n')
        if wait_for_eof:
            # operations that require "wait_for_eof" typically take a long time
            # to complete on wap-init's side (e.g. WAP provisioning may take up to
            # 10 mins). Therefore, we have to increase the default timeout so that
            # we don't time out before wap-init has responded.
            sock.settimeout(720.0) # 12 minutes time-out

        while True:
            data = sock.recv(4096)
            response = JSONRPCProtocol().parse_reply(data)
            
            print data
            if not wait_for_eof:
                if hasattr(response, 'result'):
                    return response.result, status_msg
                else:
                    return {'error': 'Error Response: ' + response.error}, status_msg
            else:
                if hasattr(response, 'result'):
                    if response.result == "END" or response.result == "DONE":
                        #print "response.result fi=", response.result
                        #print "status_msg fi=",status_msg
                        return response.result, status_msg
                    else:
                        status_msg += "<br>[%s]" % response.result
                        #print "status_msg else", status_msg 
                        
                else:
                    return {'error': 'Error Response: ' + response.error}, status_msg

    except Exception, error:
        return {'error': 'Exception: %s<br>Data Received: %s' % (str(error), str(data))}, status_msg
    finally:
        sock.close()


result, status_msg = provision_wap_conf()
print "result =", result
print "status_msg =",status_msg