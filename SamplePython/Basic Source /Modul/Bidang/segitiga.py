import math
class Segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    def SetAlas(self, a):
        self.alas = a
    def GetAlas(self):
        return self.alas
    def SetTinggi(self, t):
        self.tinggi = t
    def GetTinggi(self):
        return self.tinggi
    def GetSisiMiring(self):
        return math.sqrt(self.alas**2 + self.tinggi**2)
    def HitungKeliling(self, s):
        return self.alas + self.tinggi + s
    def HitungLuas(self):
        return (self.alas * self.tinggi) / 2