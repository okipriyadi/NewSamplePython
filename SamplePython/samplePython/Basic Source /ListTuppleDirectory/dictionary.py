print "--------------------------------Dictionary----------------------------"

print "List dengan index berupa kata kunci"
bahasa = {"arab":"Ana", "indonesia":"saya","sunda":"kuring", "jawa":"kulo"}
print bahasa["jawa"]
print bahasa["sunda"]

print "memperoleh daftar kunci & Nilai"
print bahasa.keys()
print bahasa.values()

print "pasangan kunci dan nilai berupa list"
print "memeiksa /mencari keberadaan kunci" 
print bahasa.has_key('jepang')
print bahasa.has_key('jawa')

print "memperoleh ,mencari nilai"
print bahasa.get('jawa')
print bahasa.get('jerman')

print "Ubah data dan tambah data"
bahasa.update({"sunda":"Abdi"})
print bahasa
bahasa.update({"jerman":"ich"})
print bahasa

print "Menyalin Dictionary"
bahasaCopy = bahasa
bahasa["sunda"]="Simkuring"
print bahasa
print bahasaCopy #terlihat bahwa perubahan pada bahasa juga merubah pada bahasaCopy karna sejatinya array adalah alamat memory
bahasaCopy2=bahasa.copy()
bahasa["sunda"]="Simabdi"
print bahasa
print bahasaCopy2 #terlihat bahwa perubahan pada bahasa TIDAK merubah pada bahasaCopy2 

print "Menghapus data"
del(bahasa["jerman"])
print bahasa

print "menghapus semua data"
bahasa.clear()
print bahasa

print "true or false"
print "arab" in bahasa