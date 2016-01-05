#os.environt ==> Get the users environment
#os.environ ==> A mapping object representing the string environment
import os

#For example, environ['HOME'] is the pathname of your home directory (on some platforms)
print "key home = ", os.environ['HOME']

#akan menghasilkan error karna kunci xxx tidak ada
#print "key home = ", os.environ['xxx']

#bisa juga dengan menggunakan get, bedanya get akan mereturn none jika kunci yg dicari tidak ada, sedangkan dengan cara print os.environ['HOME'] akan menhasilkan error jika key tidak ada
print "key home = ",os.environ.get('HOME')
print "key xxx tidak ada = ",os.environ.get('xxx')

#You can also use get when printing the key, useful if you want to use a default value instead of None
print "set default =>", os.environ.get('HOME','/home/username/')
print "set default =>", os.environ.get('xxx','/home/username/')
print "jika tidak diset mk kembali nilai kosong =>", os.environ.get('xxx')
#atau bisa juga dengan cara, bedanya variabel akan dibuat dan nilai default akan dimasukan ke dalam key tersebut:
os.environ.setdefault("inikuncisaya", "t3st")
print "set default =>", os.environ.get("inikuncisaya")

#ubah nilai kunci
os.environ['inikuncisaya'] = "waduhh"
print "ubah kunci ==>",  os.environ.get("inikuncisaya")

print "tampilkan seluruh kunci :"
print "==============================================="
print os.system('env')
print "==============================================="

#mendelete kunci
del os.environ['inikuncisaya']
print "delete kunci", os.environ.get('inikuncisaya')
print "==============================================="
print os.system('env')
