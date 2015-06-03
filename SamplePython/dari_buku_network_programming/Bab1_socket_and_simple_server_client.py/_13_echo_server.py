"""
First, we create the server. We start by creating a TCP socket object. Then, we set the reuse
address so that we can run the server as many times as we need. We bind the socket to the
given port on our local machine. In the listening stage, we make sure we listen to multiple
clients in a queue using the backlog argument to the listen() method. Finally, we wait for
the client to be connected and send some data to the server. When the data is received, the
server echoes back the data to the client
"""
import socket

PORT = 10001
HOST = 'localhost'
backlog = 5
data_payload = 2048

def echo_server():
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    #bind the socket to the port
    print "Starting up echo server on %s port %s" % (HOST, PORT)
    sock.bind((HOST, PORT))
    # Listen to clients, backlog argument specifies the max no. of queued connections
    sock.listen(backlog)
    while True:
        print "Waiting to receive message from client"
        client, address = sock.accept()
        print "mendapat koneksi dari client = %s, address=%s"%(client, address)
        data = client.recv(data_payload)
        if data:
            print "Data: %s" %data
            client.send(data)
            print "sent %s bytes back to %s" % (data, address)
        # end connection
        client.close()
    
    
if __name__ == "__main__":
    echo_server() 