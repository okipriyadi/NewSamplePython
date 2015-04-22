"""
Sockets transmit streams of bytes. Those bytes can contain text messages, as in the
previous examples, or they can be made up of binary data that has been encoded for
transmission. To prepare binary data values for transmission, pack them into a buffer with struct .
This client program encodes an integer, a string of two characters, and a floatingpoint 
value into a sequence of bytes that can be passed to the socket for transmission.
"""

import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, 'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)
print 'values =', values
try:
    # Send data
    print >>sys.stderr, 'sending %r' % binascii.hexlify(packed_data)
    sock.sendall(packed_data)
    
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()