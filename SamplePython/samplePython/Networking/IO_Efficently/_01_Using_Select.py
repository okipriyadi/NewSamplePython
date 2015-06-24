"""
select() makes it easier to monitor multiple connections at the same time, and it is more 
efficient than writing a polling loop in Python using socket timeouts, because the 
monitoring happens in the operating system network layer, instead of the interpreter.

The echo server example from the socket section can be extended to watch for
more than one connection at a time by using select() . The new version starts out by
creating a nonblocking TCP/IP socket and configuring it to listen on an address.
"""

import select
import socket
import sys
import Queue

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0) #setblocking() method to change the blocking flag for a socket. The default value is 1 , which means to block. Passing a value of 0 turns off blocking. If the socket has blocking turned off and it is not ready for the operation, then socket.error is raised.
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)
# Listen for incoming connections
server.listen(5)

"""
The arguments to select() are three lists containing communication channels to
monitor. The first is a list of the objects to be checked for incoming data to be read,
the second contains objects that will receive outgoing data when there is room in their
buffer, and the third includes those that may have an error (usually a combination of
the input and output channel objects). The next step in the server is to set up the lists
containing input sources and output destinations to be passed to select() .
"""

# Sockets from which we expect to read
inputs = [ server ]

# Sockets to which we expect to write
outputs = [ ]

"""
Connections are added to and removed from these lists by the server main loop.
Since this version of the server is going to wait for a socket to become writable before
sending any data (instead of immediately sending the reply), each output connection
needs a queue to act as a buffer for the data to be sent through it.
"""

# Outgoing message queues (socket:Queue)
message_queues = {}

"""
The main portion of the server program loops, calling select() to block and wait
for network activity.
"""

while inputs:
    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, 'waiting for the next event'
    readable, writable, exceptional = select.select(inputs, #incoming data to be read
                                                    outputs,#objects that will receive outgoing data when there is room in thei buffer
                                                    inputs) #includes those that may have an error (usually a combination of the input and output channel objects)
    """
    select() returns three new lists, containing subsets of the contents of the lists
    passed in. All the sockets in the readable list have incoming data buffered and avail-
    able to be read. All the sockets in the writable list have free space in their buffer and
    can be written to. The sockets returned in exceptional have had an error (the actual
    definition of "exceptional condition" depends on the platform).
    The "readable" sockets represent three possible cases. If the socket is the main
    "server" socket, the one being used to listen for connections, then the "readable" con-
    dition means it is ready to accept another incoming connection. In addition to adding
    the new connection to the list of inputs to monitor, this section sets the client socket to
    not block.
    """

    # Handle inputs
    for s in readable:
        if s is server:
            # A "readable" socket is ready to accept a connection
            connection, client_address = s.accept()
            print >>sys.stderr, ' connection from', client_address
            connection.setblocking(0)
            inputs.append(connection)
            # Give the connection a queue for data we want to send
            message_queues[connection] = Queue.Queue()
            
            """
            The next case is an established connection with a client that has sent data. The data
            is read with recv() , and then it is placed on the queue so it can be sent through the
            socket and back to the client.
            """
            
        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                print >>sys.stderr, ' received "%s" from %s' % \
                (data, s.getpeername())
                message_queues[s].put(data)
            
                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
                    
                """
                A readable socket without data available is from a client that has disconnected,
                and the stream is ready to be closed.
                """
            
            else:
                # Interpret empty result as closed connection
                print >>sys.stderr, ' closing', client_address 
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                
                # Remove message queue
                del message_queues[s]
                
    """
    There are fewer cases for the writable connections. If there is data in the queue for
    a connection, the next message is sent. Otherwise, the connection is removed from the
    list of output connections so that the next time through the loop, select() does not
    indicate that the socket is ready to send data.
    """
    
    # Handle outputs
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except Queue.Empty:
            # No messages waiting so stop checking for writability.
            print >>sys.stderr, ' ', s.getpeername(), 'queue empty'
            outputs.remove(s)
        else:
            print >>sys.stderr, ' sending "%s" to %s' % (next_msg, s.getpeername())
            s.send(next_msg)
            
    #Finally, if there is an error with a socket, it is closed
    # Handle "exceptional conditions"
    for s in exceptional:
        print >>sys.stderr, 'exception condition on', s.getpeername()
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        
        # Remove message queue
        del message_queues[s]