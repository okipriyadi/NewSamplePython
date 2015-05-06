import struct
import binascii

values = (1, 'ab', 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values 
print 'Format string :', s.format 
print 'Uses:', s.size, 'bytes'
#Pack Data
packed = binascii.hexlify(packed_data)
print 'Packed Value:', packed

#Unpack data
un_packed = binascii.unhexlify(packed)
un_packed_data =  s.unpack(un_packed)
print 'Unpacked Value =', un_packed_data