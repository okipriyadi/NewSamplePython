from construct import Struct, UBInt8, UBInt16, OptionalGreedyRange, Container

#OptionalGreedyRange(subcon) berguna agar field tersebut berupa optional yang artinya boleh kosong kalau error juga akan diisi kongong

mo_payload = Struct('mo_payload',
                     UBInt8 ('destination'),
                     UBInt8 ('flags'),
                     UBInt16('msg_id'),
                     OptionalGreedyRange(UBInt8("payload")))

payload = "Ini pesannya"
a = Container(destination=1, msg_id=1, flags=1, payload= payload)
print "a : ", a

#build
b = mo_payload.build(a)
print "b : ", b

#parse
c = mo_payload.parse(b)
print "c : ", c


print "===================================="
#lihat isi payload "ini pesannya hilang karna yang diutuhkan adalah Unsign bigendianes Integer 8 bit"
#maka bisa dengan bantuan fungsi ord yang mengubah character dalam bentuk angka
print "payload dlm bentuk symbol ASCII = ", payload
print "len = ", len(payload)
payload = map(ord, payload)
print "payload dikonversi dari symbol ke integer= ", payload
print "len = ", len(payload)
hexa = map(hex, payload)
print "dalam bentuk hexa(16) = ", hexa
print "len dalam bentuk hexa(16) = ", len(hexa)

a = Container(destination=1, msg_id=1, flags=1, payload= payload)
print "a : ", a

#build
b = mo_payload.build(a)
print "b : ", b

#parse
c = mo_payload.parse(b)
print "c : ", c
