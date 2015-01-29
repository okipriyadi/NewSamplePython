import sys

print "\n memberikan output berupa lokasi dimana interpreter kita berada"
#jika menggunakan linux hasilnya berupa ur/bin/python
#jika menggunakan windows hasilnya biasnya berupa c:\\Python27\\pythonw.exe
print sys.executable

print "\n menghasilkan platform OS"
print sys.platform

print "\n menampilkan modul yang sudah di built in sehingga kita bisa impor modul ini dalam python"
print sys.builtin_module_names

print "\n menampilkan seluruh modul beserta pathnya"
print sys.modules

print " \n menghasilkan true jika terdapat modul dalam parameter"
import time
print sys.modules.has_key('time')

print "\n menghasilkan list nama file yang seadnga aktif"
print sys.argv
print "\n menghasilkan nama file yang seadnga aktif"
print sys.argv[0]