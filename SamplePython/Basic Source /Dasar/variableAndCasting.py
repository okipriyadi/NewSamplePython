print 9/4 #karna keduanya integer maka menghasilkan INTEGER
print 9.0/4 #menghasilkan float karna salah satunya float
print float(9)/4 #pake casting juga bisa
print int(9/4) #hasilnya int, int akan membulatkan kebawah
print round(9.0/4) #hasilnya adalah hasil dengan pembulatan berdasarkan angka setelah koma. lbh kecil dr 0,5 akan membulankan ke bawah, dan sebaliknya
print round(10.0/4)
c=1
d=2
e=3
print c+d+e
print str(c) + str(d) + str(e)
f = "9"
#print f+3 
#akan menghasilkan error karna string gak bisa ditambah denga INTEGER

print int(f)+3
d = [type(c)]
d= str(d)
print d, type(d), d[0]


print "Angka dibelakang koma"
x = "12.33423423423424"
print x
y = float("{0:.3f}".format(float(x)))
print type(y)


print "\nMengkonversi dari dictionary menjadi objek"
class DBStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

A = {'A':'SDASD','B':'DASDSA','C':'WERWR','D':'ZXCZC'}
dict_konversi = DBStruct(**A)
print dict_konversi
print dict_konversi.B
print dict_konversi.D
