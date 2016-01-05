"""
ascii mempunyai 255 character
"""


 

print "karakter yang ada di ascii (tidak semua bisa ditampilkan sehingga tampilannya menjadi character aneh)"
print "========================= dari angka ke char =========================:"
a = 0

while a <= 255:
    print a ,"=", chr(a)
    a = a + 1 

print "========================= dari char ke angka ========================="
from string import letters, digits
huruf_angka = letters + digits
print "huruf = ", letters
print "angka = ", digits
print "huruf + angka =",  huruf_angka
for a in  huruf_angka:
    print a, "=", ord(a)