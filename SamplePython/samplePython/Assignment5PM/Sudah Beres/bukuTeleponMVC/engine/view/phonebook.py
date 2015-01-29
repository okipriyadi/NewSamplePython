class PhonebookView(object):

    @staticmethod
    def menu():
        print "\n======================= Sample Phonebook =================="
        print "Pilih perintah: "
        print "1. Tambah kontak"
        print "2. Cari kontak"
        print "3. Edit kontak"
        print "4. Hapus kontak"
        print "5. Tampilkan semua kontak"
        print "6. Keluar"
        print "\n-----------------------------------------------------------"
        pilihan = raw_input("Pilihan : ")
        return pilihan

    @staticmethod
    def form():
        nama = raw_input('nama : ')
        alamat = raw_input('alamat : ')
        telepon = raw_input('telepon : ')
        return {'nama': nama, 'alamat': alamat, 'telepon': telepon}

    @staticmethod
    def search():
        keyword = raw_input('keyword : ')
        return keyword

    @staticmethod
    def pilihEdit():
        edit = raw_input("Pilih nomor untuk diedit")
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