"""
When sending multibyte binary data between two systems, it is important to ensure
that both sides of the connection know what order the bytes are in and how to assemble
them back into the correct order for the local architecture. The server program uses the
same Struct specifier to unpack the bytes it receives so they are interpreted in the
correct order.
"""

import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
    print >>sys.stderr, '\nwaiting for a connection'
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print >>sys.stderr, 'received %r' % binascii.hexlify(data)
        unpacked_data = unpacker.unpack(data)
        print >>sys.stderr, 'unpacked:', unpacked_data
    finally:
        connection.close()