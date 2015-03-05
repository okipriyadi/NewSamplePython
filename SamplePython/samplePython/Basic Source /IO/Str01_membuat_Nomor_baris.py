import sys 
import string

namafile = sys.argv[0]
print "hasil path : ",namafile
print "-" * len(namafile)

file = open(namafile,"r")
jumlahbaris = len(file.readlines())
print "jumlahbaris : ", jumlahbaris
lebar = len(str(jumlahbaris))
print "lebar", lebar
file.seek(0)
n=0
for baris in file.readlines():
    n = n + 1
    nomor = string.zfill(n,lebar)
    print "%s| %s" % (nomor, baris)
file.close