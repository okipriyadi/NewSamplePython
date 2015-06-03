class persegiPanjang:
   
    def __init__(self, panjang = 1, lebar=1): #Ini adalah konstruktor, konstruktor dalam python adalah fungsi __init__
        self.panjang = panjang
        self.lebar = lebar
        
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
            
    def  __del__(self): #__del__ adalah destruktor pada python        pass
        pass




        
persegiPanjangA = persegiPanjang(20, 10)
persegiPanjangB = persegiPanjang(10, 5)

print "Panjang A: ", persegiPanjangA.panjang
print "Lebar A", persegiPanjangA.lebar
print "Panjang B: ", persegiPanjangB.panjang
print "Lebar B", persegiPanjangB.lebar

print "Luas A: ", persegiPanjangA.hitung_luas()
print "Luas B: ", persegiPanjangB.hitung_luas()

print "keliling A: ", persegiPanjangA.hitung_keliling()
print "keliling B: ", persegiPanjangB.hitung_keliling()

print "gambar A: \n", persegiPanjangA.gambar_persegi_panjang()
print "gambar A tanpa isi \n", persegiPanjangA.gambar_persegi_panjang_tanpa_isi()
