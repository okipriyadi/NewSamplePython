"""
Point-to-point connections handle a lot of communication needs, but passing the same
information between many peers becomes challenging as the number of direct connec-
tions grows. Sending messages separately to each recipient consumes additional pro-
cessing time and bandwidth, which can be a problem for applications such as streaming
video or audio. Using multicast to deliver messages to more than one endpoint at a time
achieves better efficiency because the network infrastructure ensures that the packets
are delivered to all recipients

Multicast messages are always sent using UDP, since TCP requires an end-to-end
communication channel. The addresses for multicast, called multicast groups, are a sub-
set of the regular IPv4 address range (224.0.0.0 through 230.255.255.255) reserved for
multicast traffic. These addresses are treated specially by network routers and switches,
so messages sent to the group can be distributed over the Internet to all recipients that
have joined the group.

Note: Some managed switches and routers have multicast traffic disabled by
default. If you have trouble with the example programs, check your network hard-
ware settings

This modified echo client will send a message to a multicast group and then report all
the responses it receives. Since it has no way of knowing how many responses to expect,
it uses a timeout value on the socket to avoid blocking indefinitely while waiting for an
answer

The socket also needs to be configured with a time-to-live value (TTL) for the
messages. The TTL controls how many networks will receive the packet. Set the TTL
with the IP_MULTICAST_TTL option and setsockopt() . The default, 1 , means that
the packets are not forwarded by the router beyond the current network segment. The
value can range up to 255 and should be packed into a single byte.
"""


import socket
import struct
import sys
message = 'very important data'
multicast_group = ('224.3.29.71', 10000)
# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)
# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
#The rest of the sender looks like the UDP echo client, except that it expects multiple responses 
#so uses a loop to call recvfrom() until it times out.

try:
    # Send data to the multicast group
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, multicast_group)
    # Look for responses from all recipients
    while True:
        print >>sys.stderr, 'waiting to receive'
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print >>sys.stderr, 'timed out, no more responses'
            break
        else:
            print >>sys.stderr, 'received "%s" from %s' %(data, server)
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()