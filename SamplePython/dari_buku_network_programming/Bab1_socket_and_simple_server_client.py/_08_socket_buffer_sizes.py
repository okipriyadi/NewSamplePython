"""
The default socket buffer size may not be suitable in many circumstances. In such
circumstances, you can change the default socket buffer size to a more suitable value.

Let us manipulate the default socket buffer size using a socket object's
setsockopt() method.

First, define two constants: SEND_BUF_SIZE / RECV_BUF_SIZE and then wrap a socket
instance's call to the setsockopt() method in a function. It is also a good idea to check the
value of the buffer size before modifying it. Note that we need to set up the send and receive
buffer size separately.
"""

import socket
SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    # Get the size of the socket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [Before]:%d" %bufsize
    
    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1) #The setsockopt() method takes three arguments: level , optname , and value
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [After]:%d" %bufsize

if __name__ == '__main__':
    modify_buff_size()