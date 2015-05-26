class Hello_world():
    def __init__(self):
        self.Pariabel = "saya orang sunda"
        
    def saja(self):
        print "pulangkan saja "
    
a = Hello_world()
b = getattr(a, "Pariabel")
print b

c = getattr(a, "saja")
c()


