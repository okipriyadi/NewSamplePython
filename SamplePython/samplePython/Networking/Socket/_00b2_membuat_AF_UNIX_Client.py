import socket 

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.connect ('/tmp/sock') #Koneksi ke file socket
#sock.bind('/tmp/sock')  #/tmp/sock merupakan file socket-- #FILE /tmp/socket akan dibuat secara otomatis
#sock.listen(5)
#sock.accept() #Menerima koneksi
sock.send('ini pesan dari client')
pesan = sock.recv(1024) 
print pesan #M