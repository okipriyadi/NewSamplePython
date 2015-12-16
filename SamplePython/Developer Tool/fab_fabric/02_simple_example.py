#INGAT NAMA FILENYA harus fabfile.py jika bukan makan harus menambahkan perintah -f diikuti nama file

from fabric.api import *  
env.hosts = [  
             'server1.domainmu.com',  
             'server2.domainmu.com'  
             ]

env.user   = 'userbisasudo'  

def kosongkan_tmp():  
    """ Hapus semua isi /tmp """
    run("sudo rm -rf /tmp/*")

def install_nginx():  
    """Install nginx dari default repo"""
    run("sudo aptitude install -y nginx")
    
"""
Dengan script fabfile.py diatas, terdapat 2 tugas yang akan terlihat dalam 
daftar Fabric ketika dijalankan command fab -l. 
Untuk menjalankan salah satu dari tugas dalam script tersebut adalah fab nama_tugas

=====================================
$fab install_nginx
=====================================

bisa juga
=====================================
$fab kosongkan_tmp
=====================================

atau keduanya sekaligus
=====================================
$fab kosongkan_tmp install_nginx 
=====================================

Fungsi-fungsi penting dalam Fabric untuk memulai membuat tugas administrasi penting:

run     (fabric.operations.run)
sudo    (fabric.operations.sudo)
local   (fabric.operations.local)
get     (fabric.operations.get)
put     (fabric.operations.put)
prompt  (fabric.operations.prompt)
reboot  (fabric.operations.reboot)
""" 
