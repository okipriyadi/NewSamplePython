class Ayah:
    motor = "Legenda"
    def __init__(self, x):
        self.motor = x
        
      

class Ibu:
    mobil = "karimun"
    
    """# def __init__(self, x):
    self.mobil = x"""
        
    def setMobil(self, x):
        self.mobil = x 
        
        
        
    
class Anak(Ayah, Ibu):
    def __init__(self, x):
        Ayah.__init__(self, x) 
        
        
anakPertama = Anak("2")
anakPertama.setMobil("set")
print anakPertama.mobil
print anakPertama.motor
