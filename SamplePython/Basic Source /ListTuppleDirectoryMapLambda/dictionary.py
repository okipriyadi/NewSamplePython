print "--------------------------------Dictionary----------------------------"

print "Mengakses nilai dict jika key tidak ada maka akan menghasilkan error"
bahasa = {"arab":"Ana", "indonesia":"saya","sunda":"kuring", "jawa":"kulo"}
print bahasa["jawa"]
print bahasa["sunda"]
try:
    print bahasa["jerman"]
except Exception, e:
    print "menghasilkan error karna key/kunci", e, "tidak ada" 

#lebih Aman karna tidak menghasilkan error jika key tidak tersedia
print "\nMengakses nilai dict Versi 2, jika key tidak ada maka menghasilkan None"
print bahasa.get('jawa')
print bahasa.get('jerman')


print "\nMengakases keseluruhan KEY & NILAI dengan menggunakan loop for "
for a,v in bahasa.iteritems():
    print a
    print v 
    
print "\nMengakases keseluruhan KEY & NILAI dengan menggunakan loop for Versi 2"
for a in bahasa.iteritems():
    print a
     

print "\nMengakases keseluruhan KEY saja"
print bahasa.keys()

print "\nMengakases keseluruhan NILAI saja"
print bahasa.values()

print "\nmemeiksa /mencari keberadaan kunci" 
print bahasa.has_key('jepang')
print bahasa.has_key('jawa')

print "\nmemeiksa /mencari keberadaan kunci Versi 2" 
print "arab" in bahasa
print "ana" in bahasa


print "\nUbah data dan tambah data"
bahasa.update({"sunda":"Abdi"})
print bahasa
bahasa.update({"jerman":"ich"})
print bahasa

print "\nmengubah nama key"
bahasa['sundah'] = bahasa.pop('sunda')
print bahasa

print "\nmendelete salah satu key dan valuenya"
del(bahasa['jawa'])
print "delete bahasa jawa:", bahasa

print "\nmendelete salah satu key dan valuenya Versi2"
bahasa.pop('sundah', None)
print "delete bahasa sundah:", bahasa

print "\nMenyalin Dictionary"
bahasaCopy = bahasa
#lihat ketika bahasa diubah
bahasa["jerman"]="ich lih bedih"
print bahasa
print bahasaCopy #terlihat bahwa perubahan pada bahasa juga merubah pada bahasaCopy karna sejatinya array adalah alamat memory

print "\nMenyalin Dictionary Dengan sempurna"
bahasaCopy2=bahasa.copy()
bahasa["jerman"]="ih meni pedih"
print bahasa
print bahasaCopy2 #terlihat bahwa perubahan pada bahasa TIDAK merubah pada bahasaCopy2 


print "\nMengkonversi dari dictionary menjadi objek"
class DBStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
        
dict_konversi = DBStruct(**bahasa)
print dict_konversi
print dict_konversi.jerman

print "\nMenghapus data"
del(bahasa["jerman"])
print bahasa

print "\nmenghapus semua data"
bahasa.clear()
print bahasa

print "\nmembat dictionary kosong dengan kunci list"
d = ["aa","bb","cc"]
poems = dict.fromkeys(d, '') 
print poems
