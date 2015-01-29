import json
import time
class perintahPhonebook:
   
    def __init__(self, data):
        self.dataJson = data
        self.listIndex = []
        self.hitung = 0
        self.keterangan = ''
        self.localtime = time.asctime( time.localtime(time.time()) )
    def tulis(self):
        brk = open("asset/phonebook.json", 'w+')
        brk.write(json.dumps(self.dataJson))
        brk.close()
        
    def tulisLog(self):
        berkasLog = open("asset/log.txt", 'a')
        print self.keterangan
        self.keterangan = self.keterangan + "\n"
        berkasLog.write(self.keterangan)
        berkasLog.close()
        
        
    def deleteListIndex(self):
        for itt in self.listIndex:
            self.listIndex.remove(itt)
            
    def tampilkan(self):
        print "nama \t\t\t alamat \t\t\t telepon " 
        for i in self.dataJson:
            print i['nama'],"\t\t\t", i['alamat'], "\t\t\t", i['telepon']
        
            
    def tambah(self):
        no = len(self.dataJson)+1
        nama = raw_input('nama : ')
        alamat = raw_input('alamat : ')
        telepon = raw_input('telepon : ')
        self.dataJson.append({'no': no, 'nama': nama, 'alamat': alamat, 'telepon': telepon})
        self.tulis()
        self.keterangan = "["+self.localtime +  "]" + "add : " + str(no) + " "+ nama +" "+ alamat +" "+ telepon 
        self.tulisLog()  
        
    def searching(self):
        searchNama = raw_input('cari : ')
        self.deleteListIndex()
        self.hitung = 0
        for itt in self.dataJson:
            a = str(itt.get('nama'))
            if a ==searchNama:
                if self.hitung == 0:
                    print "No \t\t\t Nama: \t\t\t Alamat: \t\t\t NoTelp: "
                print itt['no'], "\t\t\t", itt['nama'],"\t\t\t", itt['alamat'],"\t\t\t ", itt['telepon']
                self.listIndex.append(str(itt.get('no')))
                self.hitung = 1
        if self.hitung == 0:
            print "data tidak ditemukan"

    def editKontak(self):
        self.searching()
        if self.hitung ==1:
            print "Pilih no mana yang akan diedit", self.listIndex
            edit = raw_input("Pilih nomor untuk diedit")
            for itt in self.dataJson:
                a = str(itt.get('no'))
                if a ==edit:
                    print "No \t\t\t Nama: \t\t\t Alamat: \t\t\t NoTelp: "
                    print itt['no'], "\t\t\t", itt['nama'],"\t\t\t", itt['alamat'],"\t\t\t ", itt['telepon']
                    print "Pilih mana yang akan diedit"
                    print "1. nama"
                    print "2. alamat"
                    print "3. telepon"
                    pilihan = raw_input("tentukan pilihan mu: ")
                    if pilihan == "1":
                        nama = raw_input('nama : ')
                        itt.update({'nama':nama})
                    elif pilihan =="2":
                        alamat = raw_input('alamat : ')
                        itt.update({"alamat":alamat})
                    elif pilihan =="3":
                        telepon = raw_input('telepon : ')
                        itt.update({"telepon":telepon})
                    self.tulis()
                    self.keterangan = "["+self.localtime + "]" + "edit no id  = " + edit 
                    self.tulisLog()
        
    def hapusKontak(self):
        self.searching()
        if self.hitung == 1 :
            print "Pilih diantara No mana yang akan dihapus", self.listIndex
            edit = raw_input("Pilih nomor untuk dihapus")
            for itt in self.dataJson:
                a = str(itt.get('no'))
                if a ==edit:
                    print "No \t\t\t Nama: \t\t\t Alamat: \t\t\t NoTelp: "
                    print itt['no'], "\t\t\t", itt['nama'],"\t\t\t", itt['alamat'],"\t\t\t ", itt['telepon']
                    print "Yakin akan dihapus ?"
                    pilihan = raw_input("(y/n)")
                    if pilihan == "y" or "Y" or "YA" or "ya" or "Ya":
                        self.dataJson.remove(itt)
                        print "delete berhasil"
                        #agar nomor kembali urut, tidak ada yang bolong
                        no = 1
                        for itt in self.dataJson:
                            itt.update({'no':no})
                            no = no +1
                        self.tulis()
                        self.keterangan = "["+self.localtime + "]" + "delete no id  = " + edit 
                        self.tulisLog()
        
        
        
    
                    
        
    
        
        
        
#open('asset/json.txt', 'a').write(data)