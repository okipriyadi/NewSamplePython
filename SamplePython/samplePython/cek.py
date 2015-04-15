import os 
from Crypto.Cipher import Blowfish
from Crypto import Random

file_full_path = "/home/kyi/logfile.log"
file_full_path_enc = "/home/kyi/logfile_enc.log"
pword = "bebass"
bs = Blowfish.block_size
iv = Random.new().read(bs)
__cipher = Blowfish.new(pword,Blowfish.MODE_ECB,iv)
fl = open(file_full_path, "rb")
fl.seek(0)
fsize = os.path.getsize(file_full_path)
chunk = fl.read(24)
ciphertext = __cipher.encrypt(chunk)
print "encrypt = ",ciphertext

#decrypt
cleartext = __cipher.decrypt(ciphertext)
print "decrypt" , cleartext    

