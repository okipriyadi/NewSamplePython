#print "===========List================"
#a=[(1,2),(2,3),(3,4)]  
#hasil = list()
#for b in a:
#        for c in b:
#                print c
#                hasil = hasil + [c]
#                print hasil
#print "hasilnya :", hasil

#print "**************Satu Baris***********"

a=[(1,2),(2,3),(3,4)]
hasil = list()

for (x,y) in a :  hasil = hasil + [x] + [y]  

print "Hasil = ",hasil
        