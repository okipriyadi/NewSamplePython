class PhonebookView(object):

    @staticmethod
    def menu():
        print "\n======================= Sample Phonebook =================="
        print "Pilih perintah: "
        print "1. Tambah kontak"
        print "2. Tampilkan Semua Kontak"
        print "3. Cari Kontak"
        print "4. Edit kontak"
        print "5. Add Relationship"
        print "6. Tampilkan Relationship"
        print "9. Keluar"
        print "\n-----------------------------------------------------------"
        pilihan = raw_input("Pilihan : ")
        return pilihan

    @staticmethod
    def form():
        nama = raw_input('nama : ')
        alamat = raw_input('alamat : ')
        banyakTelp = raw_input("Ada berapa Nomer Telpon?")
        return {'nama': nama, 'alamat': alamat, 'banyakTelp': banyakTelp}
    
    @staticmethod
    def formRelation():
        id_person = raw_input('id_person 1 : ')
        id_person2 = raw_input('id_person 2 : ')
        relation = raw_input('relationship  :')
        return {'id_person1':id_person,'id_person2':id_person2,'relation':relation}
        
    @staticmethod
    def formTelepon():
        telepon = raw_input("Masukan No Telepon: ")
        return telepon

    @staticmethod
    def search():
        keyword = raw_input('masukan keyword untuk dicari : ')
        return keyword

    @staticmethod
    def Relationship():
        pass
    
    @staticmethod
    def pilihEdit():
        edit = []
        edit[0] = raw_input("Ketik id_person untuk diedit")
        edit[1] = raw_input("pilih id_telepon untuk diedit")
        return edit
    

    @staticmethod
    def elemenEdit():
        print "Pilih mana yang akan diedit"
        print "1. nama"
        print "2. alamat"
        print "3. telepon"
        noPilihan = raw_input("tentukan pilihan mu: ")
        if noPilihan == "1":
            nama = raw_input('nama : ')
            return {'nama':nama}
        elif noPilihan =="2":
            alamat = raw_input('alamat : ')
            return {"alamat":alamat}
        elif noPilihan =="3":
            telepon = raw_input('telepon : ')
            return {"telepon":telepon}
        
    @staticmethod
    def pilihHapus():
        hapus = raw_input("Pilih nomor untuk dihapus")
        return hapus