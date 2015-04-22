"""The related functions inet_pton() and inet_ntop() work with both IPv4 and
IPv6 addresses, producing the appropriate format based on the address family parameter
passed in.
"""

import binascii
import socket
import struct
import sys

string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed = socket.inet_pton(socket.AF_INET6, string_address)
print 'Original:', string_address
print 'Packed :', binascii.hexlify(packed)
print 'Unpacked:', socket.inet_ntop(socket.AF_INET6, packed)

"""
An IPv6 address is already a hexadecimal value, so converting the packed version
to a series of hex digits produces a string similar to the original value.
"""
