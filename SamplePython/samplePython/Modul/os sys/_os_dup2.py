"""
method dup2 menduplikasi file descriptor fd ke fd2, menutup file pertama jika memungkinkan. 

Ingat bahwa file descriptor akan di assign jika memang tersedia. Contoh dibawah akan meng-assign
1000 sebagai duplikat dari fd ketika 1000 tersedia:

os.dup2(fd, fd2)

fd adalah file descriptor yang akan di duplikasi
fd2 adalah duplikat dari file descriptor

"""
import os, sys 

#Open a file
fd = os.open("foo.txt", os.O_RDWR|os.O_CREAT )

#Write one String
os.write(fd, "This is test")

#Now duplicate this file descriptor as 1000
fd2 = 1000
os.dup2(fd, fd2)

#Now read this file from the beginning using fd2
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print "Read String is :", str

#Close file
os.close(fd)

print "Closed the file successfully"
