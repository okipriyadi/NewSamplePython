print "============================Membuat Berkas"
berkas = open("negara.txt","w+")
"""
kode akses pada open():
r = berkas hanya dapat dibaca. berkas yang dibuka harus sudah ada
w = berkas hanya dapat ditulis, jika blm ada berkas akan diciptakan, kalau berkas sudah ada isinya akan dikosongkan '
a = berkas bisa ditambah. data yang pernah terekam di file tidak akan dikosongkan, operasi yang bisa dilakaukan hanya penambahan data, jika berkas belum ada, berkas akan diciptakan
r+= operasi baca tulis. berkas harus sudah ada
w+= operasi baca tulis, isi akan dikosongkan terlebih dahulu, jika berkas tidak ada, berkas akan diciptakan
Untuk mengakses file binari, kita harus menambahkan huruf 'b' pada mode akses normal 
(wb, rb, ab).
"""
berkas.write("Indonesia \n")
berkas.write("Cina \n")
berkas.close()
print "============================Menulis langsung beberapa tulisan"
burung=open("burung.txt", "w")
burung.writelines(["beo\n","jalak\n", "kakak tua\n"])
burung.close()
print "=============================Tambah Isi File"
berkas = open("kota.txt","a") #
berkas.write("Bandung\n")
berkas.write("Kupang\n")
berkas.close()
print "============================ Edit Isi berkas"
berkas = open("burung.txt", "r+")
print berkas.read()
berkas.seek(3)
berkas.write("Mer")
berkas.seek(0)
print berkas.read()
print "=============================Menguji apakah berkas sudah ada"
def berkasada(nama_berkas):
    ada = True
    try:
        berkas = open(nama_berkas)
        berkas.close()
    except IOError:
        ada = False
        return ada


berkasada("takada")
print "===========================Baca file dengan read"
berkas=open("burung.txt")
print berkas.read(6)
print berkas.read()
berkas.close()
print "=============================Membaca berkas"
berkas = open("burung.txt", "r+")
print berkas.read()
berkas.seek(-3,2)
print berkas.read(4)
print "============================Membaca menggunakan readline"
berkas = open ("kota.txt")
print berkas.readline()
print berkas.readline()
print berkas.readlines()
berkas.close()
print "===========================Membaca menggunakan readlines"
berkas=open("kota.txt")
d=berkas.readlines()
berkas.close()
print len(d)
print d 
print "===========================Membaca keseluruhan halaman"
berkas = open("kota.txt")
baris = berkas.readline()
#buang newline di akhir String
#baris = baris[:-1]
while baris:
    print baris
    baris = berkas.readline()
    baris = baris[:-1]
berkas.close()