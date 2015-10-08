"""
Kita dapat mengkategorikan server dalam dua kelas : Iterative atau Concurrent Server. 
Untuk iterative server akan terus melaksanakan langkah-langkah berikut :

1. Tunggu sampai permintaan (request) dari client tiba.
2. Proses permintaan client.
3. Kirimkan respon (response) kembali ke client yang telah mengirim permintaan (request).
4. Kembali ke langkah 1

Masalah pada iterative server adalah ketika sedang menjalankan langkah 2. 
Selama waktu tersebut HANYA SATU client yang dilayani SEDANGKAN YANG LAINNYA MENUNGGU. 

Sedangkan untuk concurrent server akan melaksanakan langkah-langkah berikut :
1. Tunggu sampai permintaan (request) dari client tiba.
2. Jalankan  server baru  untuk  menangani  permintaan (request) dari client.  Ini dapat  dilakukan   
   dengan   membuat  proses baru  atau  menggunakan   thread tergantung dari dukungan sistem operasi 
   yang digunakan. Setelah permintaan  dilayani,  server baru tersebut akan mati.
3. Kembali ke langkah 1.


Python hanya menggunakan dua domain komunikasi, yaitu : UNIX (AF_UNIX) dan Internet (AF_INET) domain. Pengalamatan pada UNIX domain direpresentasikan sebagai string, dinamakan dalam lokal path: contoh /tmp/sock. Sedangkan pengalamatan Internet domain direpresentasikan sebagai tuple(host,port), dimana host merupakan string yang merepresentasikan nama host internet yang sah (hostname), misalnya : darkstar.drslump.net atau berupa IP address dalam notasi dotted decimal, misalnya : 192.168.1.1. Dan port merupakan nomor port yang  sah antara 1 sampai 65535. Tetapi dalam keluarga UNIX penggunaan port di bawah 1024 memerlukan akses root privileges. Sebelum menggunakan modul socket dalam Python, maka modul socket harus terlebih dahulu diimport. Berikut  contohnya :
"""

#Mengimport modul socket
import socket 
 
# Mengimport seluruh konstanta, data, dan method
from socket import *
   
# Mengimport konstanta
from socket import AF_INET, SOCK_STREAM   


