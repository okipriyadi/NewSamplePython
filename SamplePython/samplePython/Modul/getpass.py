# contoh penggunaan modul getpass
import getpass

password = getpass.getpass()
print 'Password anda : ', password

password = getpass.getpass(prompt='Inputkan password anda :')
print 'Password anda : ', Password