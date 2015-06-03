"""
If you ever need to write a low-level network application, it may be necessary to handle the
low-level data transmission over the wire between two machines. This operation requires
some sort of conversion of data from the native host operating system to the network format
and vice versa. This is because each one has its own specific representation of data.
"""

import socket
def convert_integer():
    data = 1234
    # 32-bit
    print "Original: %s => Long host byte order: %s, Network byte order: %s" %(data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print "Original: %s => Short host byte order: %s, Network byte order: %s" %(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()