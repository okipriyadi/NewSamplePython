import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = ssl.wrap_socket(s)
ssl_sock.connect(('localhost', 5000))
ssl_sock.sendall("Hello World\r\n")
data = ssl_sock.read()
print data
ssl_sock.close()