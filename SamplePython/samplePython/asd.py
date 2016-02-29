import sys
import socket, ssl
import ast
import termios
import sys, tty

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s, certfile="systemapi_201.pem",
                              ca_certs="ca.pem", 
                              cert_reqs=ssl.CERT_REQUIRED,
                              keyfile='systemapi_201.key')
try:
    ssl_sock.connect(('sgw.ffp2.net', 3128))
except Exception, e:
    print 'Exception ', e
    exit()

ssl_sock.write('{ "jsonrpc" : "2.0", "method" : "flight-event-subscribe", "id" : 1 }\r\n')

data = ast.literal_eval(ssl_sock.read())

if "subscribe" in method:
    print data
    print "Ctrl+C (kill) to stop receiving"
    try:
        ssl_sock.settimeout(2)
    except Exception,e:
        pass
    while True:
        time.sleep(0.01)
        data = None
        try:
            data = ast.literal_eval(ssl_sock.read())
        except Exception, e:
            pass
            #print e
            #exit()
        if data is not None:
            print "Method: {0}".format(data['method'])
            print "Param: {0}".format(data['params'])


try:
    print "result: {0}".format(data['result'])
except Exception:
    print "no result, data = {0}".format(data)