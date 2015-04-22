"""
The user datagram protocol (UDP) works differently from TCP/IP. Where TCP is a
stream-oriented protocol, ensuring that all the data is transmitted in the right order,
UDP is a message-oriented protocol. UDP does not require a long-lived connection, so
setting up a UDP socket is a little simpler. On the other hand, UDP messages must fit
within a single packet (for IPv4, that means they can only hold 65,507 bytes because
the 65,535-byte packet also includes header information) and delivery is not guaranteed
as it is with TCP

Since there is no connection, per se, the server does not need to listen for and accept
connections. It only needs to use bind() to associate its socket with a port and then
wait for individual messages.
"""

import socket
import sys
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Messages are read from the socket using recvfrom() , which returns the data as well as the address of the client from which it was sent.
while True:
    print >>sys.stderr, '\nwaiting to receive message' 
    data, address = sock.recvfrom(4096)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    if data:
        sent = sock.sendto(data, address)
        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)