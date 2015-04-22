"""
Communication between Parent and Child Processes
The socketpair() function is useful for setting up UDS sockets for inter-process
communication under UNIX. It creates a pair of connected sockets that can be used to
communicate between a parent process and a child process after the child is forked.
"""

import socket
import os
parent, child = socket.socketpair()
pid = os.fork()
if pid:
    print 'in parent, sending message'
    child.close()
    parent.sendall('ping')
    response = parent.recv(1024)
    print 'response from child:', response
    parent.close()
else:
    print 'in child, waiting for message'
    parent.close()
    message = child.recv(1024)
    print 'message from parent:', message
    child.sendall('pong')
    child.close()