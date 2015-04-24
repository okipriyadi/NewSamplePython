"""
Many servers have more than one network interface, and therefore, more than
one IP address. Rather than running separate copies of a service bound to each IP
address, use the special address INADDR_ANY to listen on all addresses at the same time.
Although socket defines a constant for INADDR_ANY , it is an integer value and must
be converted to a dotted-notation string address before it can be passed to bind() . As
a shortcut, use “ 0.0.0.0 ” or an empty string ( ” ) instead of doing the conversion.
"""

import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address given on the command line
server_address = ('', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()

sock.listen(1)
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()