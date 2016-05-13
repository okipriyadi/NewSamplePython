"""
mengembalikan objek proxi yang mendelegasikan ke parent atau sibling class (saudara kandung). 
Hal ini berguna untuk mengakses metode warisan yang telah diganti (overridden) dalam sebuah kelas.

ada dua kasus penggunaan yang khas untuk super. Dalam hirarki kelas dengan pewarisan tunggal, 
super bisa digunakan untuk merujuk ke kelas induk tanpa menyebut secara explisit. 

kegunaan kedua adalah mendukung multiple inheritance dalam dynamic environtment. kasus ini unik 
yang hanya bisa terjadi di python. ini memungkinkan menerapkan diagram diamond dimana beberapa 
kelas dasar menerapkan metode yang sama. 
"""

class Orangtua(object):
    def __init__(self, satu, dua):
        self.satu = satu
        self.dua = dua
        print "ortu 1"
        
class Anak(Orangtua):
    def __init__(self, tiga, empat):
        self.tiga = tiga
        self.empat = empat
        print "anak1"
        
saya = Anak('haha', 'hehe')
print "--------------------, lihat ortunya tidak terprint"
#print saya.satu  #ini akan error krena __init__ orangtua tidak didefinisikan dan telah di overide oleh __init__ anak
#print saya.dua  #ini akan error krena __init__ orangtua tidak didefinisikan dan telah di overide oleh __init__ anak
print saya.tiga
print saya.empat



print "=======================================================" 
       
class Orangtua2(object):
    def __init__(self, satu, dua):
        self.satu = satu
        self.dua = dua
        print "ortu 2"
        
class Anak2(Orangtua2):
    def __init__(self, tiga, empat):
        super(Anak2, self).__init__("dadah", 'dedeh') #parameter akan dikirimkan kepada method init pada kelas Orangtua2 bukan pada anakk
        self.tiga = tiga
        self.empat = empat
        print "anak 2"
        
saya2 = Anak2('haha', 'hehe')
print "--------------------"
print saya2.satu
print saya2.dua
print saya2.tiga
print saya2.empat