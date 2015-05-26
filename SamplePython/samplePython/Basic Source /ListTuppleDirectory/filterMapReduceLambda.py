print "--------------Fungsi Filter"
def f(x): return x % 2 != 0
d = range(1,10) 
print "data asal : ", d
print "data filter",filter(f, d )
print "--------------Fungsi map"
def kuadrat(x): return x * x
print "data map",map(kuadrat, d)
print "--------------Fungsi reduce"
def jumlah(a,b): return a+b
print "data reduce",reduce(jumlah, d)


#Python supports the creation of anonymous functions (i.e. functions that are not bound to 
#a name) at runtime, using a construct called "lambda".
print "\n\n\n--------------Fungsi lambda"
def f (x): return x**2
print "fungsi biasa", f(8)

q = lambda x: x**2
print "fungsi lambda =", q(8)


z = lambda y,g : y + g
print "data lambda",z(4,3)
print "--------------Fungsi lambda & map"
r = map(lambda x: x + 32, d)
print "data lambda =",r
print "--------------------------------------------------------------"
def tambah(x):return x+32
print map(tambah, d)