#The first step to establishing a multicast receiver is to create the UDP socket.
"""
    After the regular socket is created and bound to a port, it can be added to the
multicast group by using setsockopt() to change the IP_ADD_MEMBERSHIP option.
The option value is the 8-byte packed representation of the multicast group address
followed by the network interface on which the server should listen for the traffic,
identified by its IP address. In this case, the receiver listens on all interfaces using
INADDR_ANY .
"""

import socket
import struct
import sys
multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


#The main loop for the receiver is just like the regular UDP echo server.
# Receive/respond loop
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    print >>sys.stderr, 'received %s bytes from %s' %(len(data), address)
    print >>sys.stderr, data
    print >>sys.stderr, 'sending acknowledgement to', address
    sock.sendto('ack', address)
    
    