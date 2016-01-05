"""
The struct module includes functions for converting between strings of bytes and native Python data types 
such as numbers and strings.

Structs support packing data into strings, and unpacking data from strings using format specifiers 
made up of characters representing the type of the data and optional count and endian-ness indicators. 
For complete details, refer to the standard library documentation.

In this example, the format specifier calls for an integer or long value, a two character string, 
and a floating point number. The spaces between the format specifiers are included here for clarity, 
and are ignored when the format is compiled.
"""

import struct
import binascii


#PACKING
values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values
print 'Format string  :', s.format
print 'Uses           :', s.size, 'bytes'
print 'Packed Value   :', binascii.hexlify(packed_data)
print 'Packed Data    :', packed_data

#kebalikan hexlify
print 'Packed Value   :', binascii.unhexlify('0100000061620000cdcc2c40')
#UNPACKING
unpacked_data = s.unpack(packed_data)
print 'Unpacked Values:', unpacked_data