print "Penggunaan if"
z = raw_input("y / n : ")
if z == "y" :
    print "kamu menulis y"
elif z=="n" :
    print "kamu menulis n"
else :
    print "kamu menulis", z    


print "Penggunaan operator not & and & or"

if not z:
    print "kok kosong"
    
if z and (int(z)%2): 
    print "benar"
else :
    print "salah"
    
if z=="y" or z=="Y":
    print "bagus"