import struct
import binascii

values = (1, 'ab', 2.7)
#tentukan format dalam hal ini I = integer 2s= 2buah string, f =float
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print 'Original values:', values 
print 'Format string :', s.format 
print 'Uses:', s.size, 'bytes'
print 'packed_data :', packed_data
#Pack Data
packed = binascii.hexlify(packed_data)
print 'Packed Value:', packed

#Unpack data bisa pihin satu cara diantara 2 berikut, hasilnya sama saja
un_packed = binascii.unhexlify(packed)
un_packed_data =  s.unpack(un_packed)
print 'Unpacked Value =', un_packed_data
print "un_packed_data =", un_packed_data