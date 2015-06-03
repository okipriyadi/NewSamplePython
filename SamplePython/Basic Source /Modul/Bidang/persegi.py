class Persegi:
    def __init__(self, s):
        self.sisi = s
    #def SetSisi(self, s):
    #   self.sisi = s
    def GetSisi(self=9):
        return self.sisi9
    def HitungKeliling(self):
        return 4 * self.sisi
    def HitungLuas(self):
        return self.sisi * self.sisi
    
class persegiPanjang:
   
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar       
    def hitung_luas(self):
        return self.panjang * self.lebar
    def hitung_keliling(self):
        return (2*self.panjang)+(2*self.lebar)