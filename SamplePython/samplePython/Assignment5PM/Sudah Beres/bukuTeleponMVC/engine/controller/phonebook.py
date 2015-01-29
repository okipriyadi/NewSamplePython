from ..view.phonebook import PhonebookView
from ..model.phonebook import PhonebookModel
import re

class PhonebookController:
    data = []

    def __init__(self):
        self.read()
        self.menu()

    def read(self):
        self.phonebook = PhonebookModel()
        self.data = self.phonebook.readjson()

    def menu(self):
        pilihan = PhonebookView.menu()
        self.action(pilihan)
        if pilihan!='6':
            self.menu()
            
    def cari(self):
        keyword = PhonebookView.search()
        hitung = 0
        print '%-4s%-20s%-35s%-13s' % ("No","Nama","Alamat", "Telepon")  
        for item in self.data:
            if(re.search(keyword, item['nama'], re.IGNORECASE) or re.search(keyword, item['alamat']) or re.search(keyword, item['telepon'])):
                print '%-4s%-20s%-35s%-13s' % (item['no'],item['nama'] , item['alamat'] , item['telepon'] )
                hitung = 1
        if hitung == 0:
            print "data tidak ditemukan"
        return hitung
    
    def action(self, pilihan):
        hitung = 0
        if pilihan=='1':
            new = PhonebookView.form()
            no = len(self.data) + 1
            new.update({"no":no})
            self.data.append(new)
            self.phonebook.writejson(self.data)
        if pilihan=='2':
            self.cari()
        if pilihan=='3':
            hitung = self.cari()
            if hitung ==1:
                edit = PhonebookView.pilihEdit()
                for item in self.data:
                    noEdit = str(item.get('no'))
                    if noEdit == edit:
                        pilihanEdit = PhonebookView.elemenEdit()
                        item.update(pilihanEdit)
                self.phonebook.writejson(self.data)     
        if pilihan=='4':
            hitung = self.cari()
            if hitung == 1 :
                hapus = PhonebookView.pilihHapus()
                for item in self.data:
                    komparasiNo = str(item.get('no'))
                    if komparasiNo == hapus:
                        print '%-4s%-20s%-35s%-13s' % ("No","nama","Alamat", "Telepon") 
                        print '%-4s%-20s%-35s%-13s' % (item['no'],item['nama'] , item['alamat'] , item['telepon'] )
                        print "Yakin akan dihapus ?"
                        pilihan = raw_input("(y/n)")
                        if pilihan == "y" or "Y" or "YA" or "ya" or "Ya":
                            self.data.remove(item)
                            print "delete berhasil"
                            #agar nomor kembali urut, tidak ada yang bolong
                            no = 1
                            for itt in self.data:
                                itt.update({'no':no})
                                no = no +1
                            self.phonebook.writejson(self.data)
        if pilihan=='5':
            print '%-4s%-20s%-35s%-13s' % ("No","nama","Alamat", "Telepon") 
            for item in self.data:
                print '%-4s%-20s%-35s%-13s' % (item['no'],item['nama'] , item['alamat'] , item['telepon'] )