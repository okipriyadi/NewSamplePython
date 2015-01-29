class koordinat:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __add__(self, lain):
        return koordinat(self.x + lain.x, self.y + lain.y)
 
 
posisi1 = koordinat(5,2)
posisi2 = koordinat(3,4)
posisi3 = posisi1 + posisi2
print posisi3.x
print posisi3.y   