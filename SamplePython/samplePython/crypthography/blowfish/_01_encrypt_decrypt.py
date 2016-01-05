from Crypto.Cipher import Blowfish
"""
Blowfish menggunakan kelipatan dari 8 char, oleh karena itu teks yang akan diencrypt harus memiliki 
lebar kelipatan dari depan, jika kurang maka harus ditambahkan padding
"""

teksnya = "aku adalah"
print "teksnya =" , teksnya
print "lebarnya =", len(teksnya) 

#tambahkan padding jika tidak kelipatan 8
block_size = 8
pad = block_size - len(teksnya) % block_size
print "untuk mencapai kelipatan dari depan, maka harus ditambahkan padding sebanyak = ", pad, "karakter"
#padding yg digunakan utk contoh ini adalah chr(32) yaitu spasi, sebenarnya bebas menggunakan char apa saja.
teksnya = teksnya + pad * chr(32)
print "teksnya = ",  teksnya , "(sebenarnya ada tambahan 6 spasi setelah huruf a terakhir)"
print "lebarnya sekarang menjadi", len(teksnya)
"""
jika lebar sudah kelipatan delapan maka kita bisa encrypt menggunakan BLOWFISH_P
caranya adalah Blofish.new(kunci , mode_blowfish, ???)
"""
encrypted = Blowfish.new('12345678', Blowfish.MODE_CBC, '87654321').encrypt(teksnya)
print "setelah dieknrip menjadi =", encrypted
#ord berfungsi untuk mereturn nilai integer dari sebauh character
d = map(ord, encrypted)
print "print dala bentuk integer:",d

