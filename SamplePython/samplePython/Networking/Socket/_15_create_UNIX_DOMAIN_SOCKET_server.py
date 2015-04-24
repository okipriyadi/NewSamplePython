"""
From the programmer's perspective, there are two essential differences between using
a UNIX domain socket and an TCP/IP socket. First, the address of the socket is a path
on the file system, rather than a tuple containing the server name and port. Second,
the node created in the file system to represent the socket persists after the socket
is closed and needs to be removed each time the server starts up. The echo server
example from earlier can be updated to use UDS by making a few changes in the setup
section.
"""

import socket
import sys
import os
server_address = './uds_socket'
# Make sure the socket does not already exist
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise
    
#The socket needs to be created with address family AF_UNIX .
# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the address
print >>sys.stderr, 'starting up on %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no data from', client_address
                break
    finally:
        # Clean up the connection
        connection.close()