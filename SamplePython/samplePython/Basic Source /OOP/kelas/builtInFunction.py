class persegiPanjang:
    '''
    Sebuah kelas yang memodelkan persegi panjang.
    Mempunyai dua atribut yaitu panjang dan lebar.
    Bisa menghitung luas dan keliling.
    Bisa juga menggambar persegi panjang sesuai atribut
    '''
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    '''komentar ke 2
    '''
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        return (2*self.panjang)+(2*self.lebar)
    
    def gambar_persegi_panjang(self):
        for i in range(0, self.lebar):
            for j in range(self.panjang):
                print "*",
            print ""
            
    def gambar_persegi_panjang_tanpa_isi(self):
        for i in range (0 , self.lebar):
            if i > 0 and i < self.lebar-1:
                for j in range(0, self.panjang):
                    if j > 0 and j < self.panjang-1:
                            print ' ',
                    else:
                            print '*',
            else:
                for j in range(0, self.panjang):
                    print '*',
            print ""
            






        
persegiPanjangA = persegiPanjang(20, 10)
persegiPanjangB = persegiPanjang(10, 5)

print "Doc : ", persegiPanjang.__doc__
print "Name : ", persegiPanjang.__name__
print "Dict : ", persegiPanjang.__dict__
print "Modul : ", persegiPanjang.__module__
print "Bases : ", persegiPanjang.__bases__
print "Doc : ", persegiPanjang.__doc__
print "Dict : ", persegiPanjangA.__dict__
print "module : ",persegiPanjangA.__module__