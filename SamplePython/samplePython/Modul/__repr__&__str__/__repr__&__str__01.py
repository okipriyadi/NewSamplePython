"""
object.__repr__(self): called by the repr() built-in function and by string conversions (reverse quotes) to compute the "official" string representation of an object.
object.__str__(self): called by the str() build-in function and by the print statement to compute the "informal" string representation of an object.
"""
x = 1
print "int repr : ", repr(x)

print "int str :", str(x)

y = 'a string'
print "y: ",y
print "string repr:", repr(y)
#hasilnya "'a string'"
print "string str :",str(y)
#hasilnya 'a string'

#coba bandingkan
#eval() digunakan untuk memanggil objek sehingga bisa dimuat variabel
y2 = eval(repr(y))
print "y2: ", y2
print "bandingkan y dan y2: ", y == y2
#y3 = eval(str(y)) #akan menghasilkan error

class ClassA(object):
     def __init__(self, b=None):
         self.b = b

     def __repr__(self):
         return '%s(%r)' % (self.__class__, self.b)


class ClassB(object):
     def __init__(self, a=None):
         self.a = a

     def __repr__(self):
         return '%s(a=a)' % (self.__class__)

a = ClassA()
b = ClassB(a=a)
a.b = b
print repr(a)
print repr(b)