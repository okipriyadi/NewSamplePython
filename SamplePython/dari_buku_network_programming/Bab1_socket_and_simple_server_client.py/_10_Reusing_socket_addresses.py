"""
You want to run a socket server always on a specific port even after it is closed intentionally or
unexpectedly. This is useful in some cases where your client program always connects to that
specific server port. So, you don't need to change the server port

If you run a Python socket server on a specific port and try to rerun it after closing it once, you
won't be able to use the same port. It will usually throw an error like the following command:
Traceback (most recent call last):
File "1_10_reuse_socket_address.py", line 40, in <module>
reuse_socket_addr()
File "1_10_reuse_socket_address.py", line 25, in reuse_socket_addr
srv.bind( ('', local_port) )
File "<string>", line 1, in bind
socket.error: [Errno 98] Address already in use

The remedy to this problem is to enable the socket reuse option, SO_REUSEADDR .
After creating a socket object, we can query the state of address reuse, say an old state. Then,
we call the setsockopt() method to alter the value of its address reuse state. Then, we
follow the usual steps of binding to an address and listening for incoming client connections.
In this example, we catch the KeyboardInterrupt exception so that if you issue Ctrl + C,
then the Python script gets terminated without showing any exception message.
"""

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    # Get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print "Old sock state: %s" %old_state
    
    # Enable the SO_REUSEADDR option
    sock.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
    new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )
    print "New sock state: %s" %new_state
    
    local_port = 8282
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind( ('', local_port) )
    srv.listen(1)
    print ("Listening on port: %s " %local_port)
    
    while True:
        try:
            connection, addr = srv.accept()
            print 'Connected by %s:%s' % (addr[0], addr[1])
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print '%s' % (msg,)

if __name__ == '__main__':
    reuse_socket_addr()

