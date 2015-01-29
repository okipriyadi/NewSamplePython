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
print "--------------Fungsi lambda"
z = lambda y,g : y + g
print "data lambda",z(1,1)
print "--------------Fungsi lambda & map"
r = map(lambda x: x + 32, d)
print "data lambda =",r
print "--------------------------------------------------------------"