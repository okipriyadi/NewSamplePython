"""
fungsi poll() mempunyai fitur yang hampir sama dengan select(), tapi lebih efisien. 
Kekurangannya poll() tidak bisa digunakan di sistem operasi window.  

"""

import select
import Queue
import sys 
import socket

#create TCP IP socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#setblocking
server.setblocking(0)
server_address = ('localhost', 10000)
print sys.stderr, 'starting server %s port %s' % server_address
server.bind(server_address)

#listen for incoming connection
server.listen(5)

# Keep up with the queues of outgoing messages
message_queues = {}
"""
The timeout value passed to poll() is represented in milliseconds, instead of
seconds, so in order to pause for a full second, the timeout must be set to 1000 .
"""
# Do not block forever (milliseconds)
TIMEOUT = 1000

"""
Python implements poll() with a class that manages the registered data channels
being monitored. Channels are added by calling register() , with flags indicating
which events are interesting for that channel. The full set of flags is listed in Table 11.1.

event         Description
POLLIN        Input Ready
POLLPRI       Priority Input Ready
POLLOUT       Able to receive output
POLLERR       Error
POLLHUP       Channel Closed
POLLNVAL      Channel not Open

The echo server menyeting sockets hanya untuk reading ATAU
read-write. The appropriate combinations of flags are saved to the local
variables READ_ONLY and READ_WRITE .
"""
#Commonly used flag sets 
READ_ONLY = (select.POLLIN |
             select.POLLPRI |
             select.POLLHUP |
             select.POLLERR 
             )
READ_WRITE = READ_ONLY | select.POLLOUT

#The server socket diregistrasi jadi setiap ada koneksi yang masuk maka akan men-triggers sebuah event.
# Set up the poller
poller = select.poll()
poller.register(server, READ_ONLY)

"""
poll() mer-returns sebuah tupples yang berisi file descriptor untuk socket
dan juga event flag. Mapping dari file descriptor numbers ke objects 
dibutuhkan untuk mendapatkan socket untuk read atau write.
"""
# Map file descriptors to socket objects
fd_to_socket = { server.fileno(): server,}

"""
The server's loop calls poll() and then processes the “events” returned by look-
ing up the socket and taking action based on the flag in the event.
"""
while True:
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, 'waiting for the next event'
    events = poller.poll(TIMEOUT)
    for fd, flag in events:
        # Retrieve the actual socket from its file descriptor
        s = fd_to_socket[fd]

        """
        As with select() , when the main server socket is “readable,” that really means
        there is a pending connection from a client. The new connection is registered with the
        READ_ONLY flags to watch for new data to come through it.
        """
        
        # Handle inputs
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                # A readable socket is ready to accept a connection
                connection, client_address = s.accept()
                print >>sys.stderr, ' connection', client_address
                connection.setblocking(0)
                fd_to_socket[ connection.fileno() ] = connection
                poller.register(connection, READ_ONLY)
                
                # Give the connection a queue for data to send
                message_queues[connection] = Queue.Queue()
                
                """
                Sockets other than the server are existing clients with data buffered and waiting to
                be read. Use recv() to retrieve the data from the buffer.
                """
                
            else:
                data = s.recv(1024)
                """
                If recv() returns any data, it is placed into the outgoing queue for the socket, and
                the flags for that socket are changed using modify() so poll() will watch for the
                socket to be ready to receive data.
                """
                if data:
                    # A readable client socket has data
                    print >>sys.stderr, ' received "%s" from %s' % \
                    (data, s.getpeername())
                    message_queues[s].put(data)
                    # Add output channel for response
                    poller.modify(s, READ_WRITE)
                    
                """ 
                An empty string returned by recv() means the client disconnected, so
                unregister() is used to tell the poll object to ignore the socket.
                """
                else:
                    # Interpret empty result as closed connection
                    print >>sys.stderr, ’ closing’, client_address
                    # Stop listening for input on the connection
                    poller.unregister(s)
                    s.close()
                    
                    # Remove message queue
                    del message_queues[s]
                    
        """
        The POLLHUP flag indicates a client that “hung up” the connection without closing
        it cleanly. The server stops polling clients that disappear.
        """
        
        elif flag & select.POLLHUP:
            # Client hung up
            print >>sys.stderr, ’ closing’, client_address, ’(HUP)’
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()
            
        """
        The handling for writable sockets looks like the version used in the example for
        select() , except that modify() is used to change the flags for the socket in the
        poller, instead of removing it from the output list.
        """
        elif flag & select.POLLOUT:
            # Socket is ready to send data, if there is any to send.
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                # No messages waiting so stop checking
                print >>sys.stderr, s.getpeername(), ’queue empty’
                poller.modify(s, READ_ONLY)
            else:
                print >>sys.stderr, ’ sending "%s" to %s’ %(next_msg, s.getpeername())
                s.send(next_msg)
                
        """
        And, finally, any events with POLLERR cause the server to close the socket.
        """
        elif flag & select.POLLERR:
            print >>sys.stderr, ’ exception on’, s.getpeername()
            
            # Stop listening for input on the connection
            poller.unregister(s)
            s.close()
            
            # Remove mesage queue
            del message_queues[s]