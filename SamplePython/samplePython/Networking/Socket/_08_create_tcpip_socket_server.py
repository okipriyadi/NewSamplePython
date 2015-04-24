"""
Sockets can be configured to act as a server and listen for incoming messages, or con-
nect to other applications as a client. After both ends of a TCP/IP socket are connected,
communication is bidirectional.
Echo Server
This sample program, based on the one in the standard library documentation, receives
incoming messages and echos them back to the sender. It starts by creating a TCP/IP
socket.
"""
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
#Then bind() is used to associate the socket with the server address. In this case, the address is localhost , referring to the current server, and the port number is 10000.
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection. 
sock.listen(1) #The integer argument is the number of connections the system should queue up in the background before rejecting new clients. This example only expects to work with one connection at a time.
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept() #accept() returns an open connection between the server and client, along with the client address. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall() .
    
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)#Data is read from the connection with recv() and transmitted with sendall()
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                #data = "message : '" + data + "' , sudah diterima"
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no data from', client_address
                break
    #When communication with a client is finished, the connection needs to be cleaned up using close() . This example uses a try:finally block to ensure that close() is always called, even in the event of an error.
    finally:
        # Clean up the connection
        connection.close()
        

