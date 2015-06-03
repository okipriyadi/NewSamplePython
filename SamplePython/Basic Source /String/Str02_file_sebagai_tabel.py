import string
import sys 

namafile = sys.argv[0]
pemisah = ";"
file = open(namafile, "r")
maks = {}
for baris in file.readlines():
    #splitfield berguna untuk memecah suatu string menjadi sualtu list
    record  = string.splitfields(baris, pemisah)
    kolom = -1 
    for nilai in record:
        kolom = kolom + 1
        panjang = len(nilai)
        if not maks.has_key(kolom) or panjang >maks[kolom]:
            maks.update({kolom:panjang})
file.seek(0)
for baris in file.readlines():
    record = string.splitfields(baris, pemisah)
    kolom = -1
    for nilai in record:
        kolom = kolom +1
        #strip berfungsi menghapus karakter yang tidak terlihat seperti \n \t dan spasi " " di kiri atau kanan string
        #untuk menghapus yang kirinya saja digunakan lstrip()
        #sedangkan untuk menghapus yang kanan digunakan  rstrip()
        s = string.strip(nilai)
        #ljust() = left justify, rjust()=right justify
        print string.ljust(s, maks[kolom]),
    print
file.close()    
    
