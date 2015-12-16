berkas = open("client.log")
baris = berkas.readline()
while baris:
    if "PA" in baris:
        print baris
    baris = berkas.readline()
    baris = baris[:-1]
berkas.close()
  
