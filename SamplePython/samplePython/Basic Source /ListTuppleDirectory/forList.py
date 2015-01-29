print "===========List================"

a=[(1,2),(2,3),(3,4)]
hasil = list()

for b in a: 
        print "b = ", b
        for c in b:
                print "c = ", c
                hasil = hasil + [c]
                print "hasil = ", hasil
        print "=============="
print hasil

print "**************Satu Baris***********"

a=[(1,2),(3,4),(5,6)]
hasil = list()

for (x,y) in a :
        hasil = hasil + [x] + [y]
        print "\n",hasil
        print "hmm"