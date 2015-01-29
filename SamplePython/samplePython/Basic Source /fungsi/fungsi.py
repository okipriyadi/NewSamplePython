print "cara mendeklarasikan fungsi"
def garis(): #tanpa adanya parameter, fungsi ini disebut dengan fungsi statis
    print "-" * 10

#program utama
garis()
print "ini baris ke satu"
garis()
print "ini garis kedua"
garis()
print "ini baris ketiga"

print "\n berikut fungsi dengan parameter"
def garis2(n): #tanpa adanya parameter, fungsi ini disebut dengan fungsi statis
    print "-" * n
    
garis2(5)
print "ini baris ke satu"
garis2(10)
print "ini garis kedua"
garis2(15)
print "ini baris ketiga"



print "contoh fungsi rekursif"
def faktorial(n):
    if n <= 1 : return 1
    else : return n * faktorial(n-1)
    
print faktorial(5)


