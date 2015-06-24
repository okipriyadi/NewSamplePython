print "Satu baris cuman gini doank" #print satu baris
print "Kalau yang ini untuk print beberapa baris yang ter- \
lalu panjang, makanya pake tanda back slash dan ingat setelah \
back slash tidak boleh ada karakter lain termasuk spasi"

print "doesn't"
print 'doesn\'t' #kalau jenis kutipnya sama maka harus diawali dengan backslash
print """multiple baris
baris 1
    baris 2
        baris 3 
""" 

print "Operasi tambah, dan kali pada string"
a="saya"
b="Oki"
print a+ " "+b
print (a+ " "+b + " ")*3

"Beda penjumlahan integer dengan string"
c=1
d=2
e=3
print c+d+e
print str(c) + str(d) + str(e)




""" Ini Belum Berhasil
#untuk mencetak angka dengan format rupiah gunakan:
#import locale
#locale.setlocale(locale.LC_ALL, "")
#id_ID berarti Indonesia
#print local.format("%.2f", 1234,5678, 1)
"""
