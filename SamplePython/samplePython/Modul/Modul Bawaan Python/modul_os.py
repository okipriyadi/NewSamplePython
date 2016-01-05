import os
from macpath import curdir
from duplicity.globals import rename

print "\n mencetak seluruh variabel lingkungan"
print os.environ

print "\n berisi nama operasi yang digunakan"
print os.name

print "\n menghasilkan alamat direktory kerja"
print os.getcwd()

print os.curdir

print "\n menghasilkan isi direktory dir berupa list"
print os.listdir(".")

print "\n mengubah berkas dari nama lama menjadi baru"
#os.rename("bing", "test") #("lama","baru")

print "\n berguna untuk mengubah mode berkas"
#os.mkdir(direktorinya)

print "\n berguna untuk menghapus berkas"
#os.rmdir(direktorinya)

print "\n berguna untuk menghapus mode berkas beserta isi didalamnya"
#os.mkdir(direktorinya)

print "\n menghasilkan true jika path adalah berkas"
print os.path.isfile("modul_sys.py")

print "\n menghasilkan true jika path adalah direktory"
print os.path.isdir("test")

print "\n menghasilkan true jika path adalah direktory atau berkas"
print os.path.exists("test")

#Untuk split path dari suatu file, hasil berupa tuple
#os.path.split("path")


#memberikan nama file dari path
#os.path.basename("path")

#memberikan nama direktory dari path
#os.path.dirname("path")



