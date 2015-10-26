#--------------------------------LIST----------------------------
#Value dalam list dapat diubah

iniList = [1,3,5,7]
iniListCampuran = [2157, "Oki Priyadi", ["S.Kom", "M.Kom"]]
print iniList
print iniListCampuran

print "Akses Elemen"
print iniList[0]
print iniList[1]
print iniList[1:4]
print iniList[2:]
print iniList[:3]
print iniList[-1]
print iniList[-2:]
print iniList[:-2]

print "Akses Elemen List dalam List"
print iniListCampuran[0]
print iniListCampuran[1]
print iniListCampuran[2][0]
print iniListCampuran[2][1]

print "Ubah data"
iniListCampuran[1]="okinamasay"
print iniListCampuran

print "Mengetahui Jumlah Elemen"
print len(iniList)
print len(iniListCampuran)

print "Menambah Elemen List"
iniList.append(9)
print iniList

print "menyisipkan List"
iniList.insert(2,8)
print iniList
 
print "Mengurangi Elemen List"
del(iniList[2])
print iniList

print "membalikan urutan dalam list"
iniList.reverse()
print iniList

print "mengurutkan Elemen dalam list"
iniList.sort()
print iniList