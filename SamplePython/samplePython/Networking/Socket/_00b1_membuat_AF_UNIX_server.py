"""
MEMBUAT SOCKET
---------------
Socket dibuat melalui pemanggilan 
============================================
socket(family, type[, Proto]).
============================================  
Keluarga (Family) Protokol
1. AF_UNIX    : Unix Domain Protocol
2. AF_INET    : IPv4 Protocol
3. AF_INET6   : IPv6 Protocol

Konstanta Type Socket:
1. SOCK_STREAM   : Stream Socket (TCP)
2. SOCK_DGRAM    : Datagram Socket (UDP)
3. SOCK_RAW      : Raw Socket
4. SOCK_RDM      : -
5. SOCK_SEQPACKET: -

Untuk proto bersifat opsional dan biasanya bernilai 0. 
Untuk membuat socket stream (TCP) internet domain digunakan statement berikut :
============================================
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
============================================

Jika SOCK_STREAM diganti dengan SOCK_DGRAM berarti membuat socket datagram (UDP). 
============================================
 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
============================================

Kemudian untuk membuat socket stream dalam UNIX domain :
============================================
 sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
============================================




MENGHUBUNGKAN SOCKET (Connecting)
----------------------------------
Sebuah server dari sudut pandang kita adalah sebuah proses yang mendengarkan (listen) pada port tertentu.
Ketika proses lain ingin berhubungan dengan server atau menggunakan layanan server, 
maka proses harus terhubung dengan alamat dan nomor port tertentu yang dispesifikasikan oleh server. 
Ini dilakukan dengan memanggil metode socket connect(address), dimana address adalah sebuah tuple 
(host, port) untuk Internet domain dan pathname untuk UNIX domain. Berikut contohnya :
============================================
 sock.connect (('localhost',12345)) atau
 sock.connect (('192.168.1.1',12345))
============================================

Sedangkan untuk UNIX domain,
============================================
 sock.connect ('/tmp/sock') #Koneksi ke file socket
============================================


MENGIKAT SOCKET KE PORT (BINDING)
--------------------------------

Setelah socket berhasil dibuat, maka Python akan mengembalikan sebuah socket descriptor. 
Sebelum digunakan, maka socket harus diikatkan (binding) ke alamat dan nomor port yang sesuai 
agar proses lain dapat ditujukan ke socket. Berikut ini contoh untuk binding socket pada internet domain  :
============================================ 
 sock.bind(('localhost',12345)) atau
 sock.bind(('192.168.1.1',12345))
============================================


Sedangkan untuk mengikatkan (binding) socket pada UNIX domain digunakan :
============================================ 
 sock.bind('/tmp/sock')  #/tmp/sock merupakan file socket--
============================================
Perintah di atas akan membuat file pipe /tmp/sock yang dapat digunakan 
untuk berkomunikasi antara server dan client.




MENDENGARKAN KONEKSI (Listening)
--------------------------------
Setelah socket diikatkan (bind), langkah selanjutnya adalah memanggil method listen(queue). 
Perintah ini mengistruksikan socket untuk listen pada port-port yang telah diikatkan (bind), 
dan queue merupakan sebuah integer yang merepresentasikan maksimum antrian koneksi, 
berikut contoh penggunaannya :
============================================ 
 sock.listen(5) #Mendengarkan koneksi dengan maksimum 
                 antrian sebanyak 5
============================================


MENERIMA KONEKSI (Accepting) / connection made
--------------------------------
Untuk menerima koneksi dari permintaan (request) client  pada koneksi yang menggunakan 
socket stream (TCP). Method yang digunakan accept(), berikut contoh penggunaannya :
============================================
 sock.accept() #Menerima koneksi
============================================

Statement di atas akan mengembalikan sebuah tuple (conn, address) dimana conn adalah objek socket baru 
yang berguna untuk mengirim dan menerima data dari koneksi, dan address merupakan alamat dari client.





MENGIRIM DATA KE KONEKSI (Sending)
--------------------------------  
Menerima koneksi tidak akan berarti tanpa digunakan untuk mengirim dan menerima data. 
Oleh karena itu digunakan method send(string) untuk socket stream (TCP) dan sendto(string,address) 
untuk socket datagram (UDP). Berikut ini penggunaannya untuk socket stream.
============================================
 sock.send('ini pesan dari server')
============================================

Sedangkan untuk socket datagram digunakan :
============================================
 sock.sendto('pesan dari server' , ('192.168.1.1' , 12345))
============================================ 





Menerima Data Dari Koneksi (Receiving) /DATA_RECEIVED
--------------------------------
Untuk menerima data yang dikirim dari server digunakan method recv(bufsize) untuk socket stream 
dan recvfrom(bufsize). Berikut ini penggunaannya untuk socket stream :
============================================ 
 sock.recv(1024)  #Menerima data sebesar 1024 byte
============================================
Statement di atas akan MENGAMBIL data yang dikirimkan oleh client. 
Sedangkan untuk socket datagram :
============================================
 sock.recvfrom(1024) #Menerima data sebesar 1024 byte
============================================
Statement di atas akan mengembalikan dua buah field yaitu data, address.


Menutup Koneksi (Closing)
--------------------------------
       Untuk menutup koneksi yang telah dibuat digunakan method close(s). Berikut penggunaanya :
 sock.close() #Menutup koneksi
"""

import socket 

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#sock.connect ('/tmp/sock') #Koneksi ke file socket
sock.bind('/tmp/sock')  #/tmp/sock merupakan file socket-- #FILE /tmp/socket akan dibuat secara otomatis
sock.listen(5)
sock.accept() #Menerima koneksi
sock.send('ini pesan dari server')
pesan = sock.recv(1024) 
print pesan #Menerima data sebesar 1024 byte