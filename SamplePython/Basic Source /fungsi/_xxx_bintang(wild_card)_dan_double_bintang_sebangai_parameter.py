"""
pada python *args dan **kwargs sangat umum digunakan.sebagai parametr fungsi
*args akan menghasilkan sebuah tuple
**kwargs akan menghasilkan sebuah dictionary


fungsi lain dari *args juga sebagai peng ekstract niali
"""
print "penggunaan *args:"
def foo(*args):
    for a in args:
        print a  
        
foo(1,2,3,4,5,6)


print "\npenggunaan **kwargs:"
def foo_fighter(**kwargs):
    for a in kwargs:
        print a ,"=", kwargs[a]   
        
foo_fighter(nami='oki', nami_pengker='priyadi', cekap='atos_weh')




#fungsi lain dari *args juga sebagai peng ekstract niali
print "\npenggunaan *args untuk mengextract:"
asd = (1,2,3,4)
def nirvana(a,b,c,d):
    print a 
    print b
    print c
    print d
    
nirvana(*asd)
