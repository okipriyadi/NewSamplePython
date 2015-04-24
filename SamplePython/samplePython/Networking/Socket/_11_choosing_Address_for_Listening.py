"""
It is important to bind a server to the correct address so that clients can communicate
with it. The previous examples all used 'localhost' as the IP address, which limits
connections to clients running on the same server. Use a public address of the server,
such as the value returned by gethostname() , to allow other hosts to connect. This
example modifies the echo server to listen on an address specified via a command line
argument.
"""
import socket
import sys
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()