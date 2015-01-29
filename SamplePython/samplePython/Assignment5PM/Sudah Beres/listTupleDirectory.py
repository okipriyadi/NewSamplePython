#--------------------------------LIST----------------------------
#Value dalam list dapat diubah

iniList = [1,3,5,7]
iniListCampuran = [2157, "Oki Priyadi", ["S.Kom", "M.Kom"]]
print iniList
print iniListCampuran

print "Akses Elemen"
print iniList[0]
print iniList[1]

print "Akses Elemen List dalam List"
print iniListCampuran[0]
print iniListCampuran[1]
print iniListCampuran[2][0]
print iniListCampuran[2][1]

print "Ubah data"
iniListCampuran[1]="okinamasay"
print iniListCampuran
#Mengetahui Jumlah Elemen
print len(iniList)
print len(iniListCampuran)
#Menambah Elemen List
iniList.append(9)
print iniList
#menyisipkan List
iniList.insert(2,8)
print iniList
#Mengurangi Elemen List
del(iniList[2])
print iniList
#--------------------------------Tuple----------------------------
#Value dalam list TIDAK DAPAT dapat diubah
tutuple=(1,2,3,4)
print tutuple
#Mengetahui Jumlah elemen
print len(tutuple)
#Akses elemen tuple
print tutuple[0]
print tutuple[2:4]
print tutuple[-1:]
print tutuple[1:]
#penambahan tuple
tutuple=tutuple + (7,9)
print tutuple
tutuple =tutuple*3
print tutuple
#--------------------------------Tuple----------------------------
#List dengan index berupa kata kunci
bahasa = {"arab":"Ana", "indonesia":"saya","sunda":"kuring", "jawa":"kulo"}
print bahasa["jawa"]
print bahasa["sunda"]
#memperoleh daftar kunci & Nilai
print bahasa.keys()
print bahasa.values()
#pasangan kunci dan nilai berupa list
#memeiksa keberadaan kunci 
print bahasa.has_key('jepang')
print bahasa.has_key('jawa')
#memperoleh nilai
print bahasa.get('jawa')
print bahasa.get('jerman')
#Ubah data dan tambah data
bahasa.update({"sunda":"Abdi"})
print bahasa
bahasa.update({"jerman":"ich"})
print bahasa
#Menyalin Dictionary
bahasaCopy = bahasa
bahasa["sunda"]="Simkuring"
print bahasa
print bahasaCopy #terlihat bahwa perubahan pada bahasa juga merubah pada bahasaCopy karna sejatinya array adalah alamat memory
bahasaCopy2=bahasa.copy()
bahasa["sunda"]="Simabdi"
print bahasa
print bahasaCopy2 #terlihat bahwa perubahan pada bahasa TIDAK merubah pada bahasaCopy2 
#Menghapus data
del(bahasa["jerman"])
print bahasa
#menghapus semua data
bahasa.clear()
print bahasa
#tru or false
print "arab" in bahasa