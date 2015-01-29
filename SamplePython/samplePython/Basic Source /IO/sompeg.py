daftar_pegawai = [("11234", "Amir Hamzah", 2200000),
                  ("11235", "Fatimah", 1300000),
                  ("11236", "Fika Ariyanti", 80000),
                  ("11237", "Dewi Fadlillh", 1300000),
                  ("11238", "Joni Ardian", 70000)]

berkas_peg = open("pegawai.txt","w")

for pegawai in daftar_pegawai :
    format = "%-5s%-20s%8d" % \
              (pegawai[0], pegawai[1], pegawai[2])
    berkas_peg.write(format)

berkas_peg.close()
print "data pegawai telah disimpan"