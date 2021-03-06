"""
You have decided to write an asynchronous Python socket server application. The server will
not block in processing a client request. So the server needs a mechanism to deal with each
client independently.

Python 2.7 version's SocketServer class comes with two utility classes: ForkingMixIn
and ThreadingMixIn . The ForkingMixin class will spawn a new process for each client
request. This class is discussed in this section. The ThreadingMixIn class will be discussed
in the next section. For more information, you can refer to the Python documentation at
http://docs.python.org/2/library/socketserver.html .

We can utilize the subclasses of the SocketServer class family.
It has ready-made TCP, UDP, and other protocol servers. We can create a ForkingServer
class inherited from TCPServer and ForkingMixin . The former parent will enable our
ForkingServer class to do all the necessary server operations that we did manually before,
such as creating a socket, binding to an address, and listening for incoming connections. Our
server also needs to inherit from ForkingMixin to handle clients asynchronously.
The ForkingServer class also needs to set up a request handler that dictates how to
handle a client request. Here our server will echo back the text string received from the
client. Our request handler class ForkingServerRequestHandler is inherited from the
BaseRequestHandler provided with the SocketServer library.
We can code the client of our echo server, ForkingClient , in an object-oriented fashion.
In Python, the constructor method of a class is called __init__() . By convention, it takes a
self-argument to attach attributes or properties of that particular class. The ForkingClient
echo server will be initialized at __init__() and sends the message to the server at the
run() method respectively.

In order to test our ForkingServer class, we can launch multiple echo clients and see how
the server responds back to the clients.
"""

import os
import socket
import threading
import SocketServer


SERVER_HOST = 'localhost'
SERVER_PORT = 5555 # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!'

class ForkedClient():
    """ A client to test forking server"""
    def __init__(self, ip, port):
        # Create a socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server  
        self.sock.connect((ip, port))

    def run(self):
        """ Client playing with the server"""
        # Send the data to server
        current_process_id = os.getpid()
        print 'PID %s Sending echo message to the server : "%s"' % (current_process_id, ECHO_MSG)
        sent_data_length = self.sock.send(ECHO_MSG)
        print "Sent: %d characters, so far..." %sent_data_length
        # Display server response
        response = self.sock.recv(BUF_SIZE)
        print "PID %s received: %s" % (current_process_id, response[5:])
        
    def shutdown(self):
        """ Cleanup the client socket """
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # Send the echo back to the client
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print "Server sending response [current_process_id: data] = [%s]" %response
        self.request.send(response)
        return

class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer,):
    """Nothing to add here, inherited everything necessary from parents"""
    pass

def main():
    # Launch the server
    server = ForkingServer((SERVER_HOST, SERVER_PORT),ForkingServerRequestHandler)
    ip, port = server.server_address # Retrieve the port number
    print ip, port
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.setDaemon(True) # don't hang on exit
    server_thread.start()
    print 'Server loop running PID: %s' %os.getpid()
    
    # Launch the client(s)
    client1 = ForkedClient(ip, port)
    client1.run()
    client2 = ForkedClient(ip, port)
    client2.run()
    # Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()
    
    #import time
    #time.sleep(15)
        
if __name__ == '__main__':
    main()