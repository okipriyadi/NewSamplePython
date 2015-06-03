"""
Perhaps you prefer writing a multi-threaded application over a process-based one due to any
particular reason, for example, sharing the states of that application across threads, avoiding
the complexity of inter-process communication, or something else. In such a situation, if you
like to write an asynchrono


As seen in the previous socket server based on ForkingMixIn , ThreadingMixIn
socket server will follow the same coding pattern of an echo server except a few things.
First, our ThreadedTCPServer will inherit from TCPServer and TheadingMixIn . This
multi-threaded version will launch a new thread when a client connects to it. Some more
details can be found at http://docs.python.org/2/library/socketserver.html.

The request handler class of our socket server, ForkingServerRequestHandler , sends
the echo back to the client from a new thread. You can check the thread information here. For
the sake of simplicity, we put the client code in a function instead of a class. The client code
creates the client socket and sends the message to the server.
"""

import os
import threading
import socket
import SocketServer


SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUFF_SIZE = 1024

def client(ip, port, message):
    """a client """
    sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try :
        sock.sendall(message)
        print "message : %s dikirim ke server" % message 
        response = sock.recv(BUFF_SIZE)
        print "Client received: %s" %response
    finally:
        sock.close()
        
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """ An example of threaded TCP request handler """
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        response = "%s: %s" %(current_thread.name, data)
        self.request.sendall(response)
        
        
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""
    pass


if __name__ == "__main__":
    # Run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address # retrieve ip address
    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" %server_thread.name
    # Run clients
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")
    # Server cleanup
    server.shutdown()