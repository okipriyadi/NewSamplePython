import sys, os

if len(sys.argv) != 3:
    sys.stderr.write("Penggunaan: kopifile sumber hasil ")
    sys.exit(1)
    
nama_sumber = sys.argv[1]
nama_target = sys.argv[2]

if  not os.path.isfile(nama_sumber):
    sys.stderr.write("berkas sumber tidak ada")
    sys.exit(2)
    
if os.path.exists(nama_target):
    sys.stderr.write("Berkas target sudah ada")
    sys.exit(3)

#proses penyalinan 
try: 
    berkas_sumber = open(nama_sumber, "rb")
    berkas_target = open (nama_target,"wb")
    data = berkas_sumber.read(10240) #baca per 10KB
    while data:
        berkas_target.write(data)
        data = berkas_sumber.read(10240)
    berkas_sumber.close()
    berkas_target.cloase()
    print "Penyalinan selesai"
    
except:
    sys.stderr.write("Gagal menyimpan")
    sys.exit(4)
    
sys.exit(0)     