#Menggabungkan path, python akan menyesuaikan dengan system operasi yang dipakai
import os
p = os.path.join("c:/","saya")
q = os.path.join("c:","saya")
r = os.path.join("c","saya")
s = os.path.join("c:","saya","1","2", "3")
t = os.path.join("c:","saya","/1","/2", "3")
print p
print q
print r
print s
print t