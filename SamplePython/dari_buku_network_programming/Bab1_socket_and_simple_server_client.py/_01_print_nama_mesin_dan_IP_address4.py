import socket
hostname = socket.gethostname()
print hostname
alamat_ip = socket.gethostbyname(hostname)
print alamat_ip