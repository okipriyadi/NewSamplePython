import json
from modul import perintahPhonebook

pilihan = ''
data = []

try: 
    berkas = open("asset/phonebook.json", 'r+')
    
except:
    #Jika File Belum ada, maka buat file
    berkas = open("asset/phonebook.json", 'w+')
    

tmp = berkas.read()
berkas.close()

if tmp!='':
    data = json.loads(tmp)


while pilihan!='6':
    print "\n======================= Sample Phonebook =================="
    print "Pilih perintah: "
    print "1. Tambah kontak"
    print "2. Cari kontak"
    print "3. Edit kontak"
    print "4. hapus kontak"
    print "5. tampilkan semua kontak"
    print "6. keluar"
    pilihan = raw_input("Pilihan : ")
   
   
    objekKontak = perintahPhonebook(data)
    if pilihan=='1':
        objekKontak.tambah()
        
    if pilihan=='2':
        objekKontak.searching()
        
    if pilihan=='3':
        objekKontak.editKontak()
                    
    if pilihan =="4":
        objekKontak.hapusKontak()
                                    
    if pilihan=='5':
        objekKontak.tampilkan()
                     
