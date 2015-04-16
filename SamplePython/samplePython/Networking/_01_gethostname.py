"""
port numbers for network services with standardized names can be looked up using getservbyname() .
To reverse the service port lookup, use getservbyport().

socket class = for handling the actual data channel, and also includes functions for network-related tasks, 
such as converting a servers name to an address and formatting data to be sent across the network

Sockets have two primary properties controlling the way they send data: 
1. the address family => controls the OSI network layer protocol used, 
2. the socket type => controls the transport layer protocol

Python supports three address families. 
1. AF_INET , is used for IPv4 Internet addressing.
2. AF_INET6 is used for IPv6 Internet addressing.
3. AF_UNIX is the address family for UNIX Domain Sockets (UDS)

The socket type is usually either :
1. SOCK_DGRAM for user datagram protocol (UDP)
2. SOCK_STREAM for transmission control protocol (TCP)
"""
import socket
"""
Use gethostbyname() to consult the operating system hostname resolution API
and convert the name of a server to its numerical address.
"""
print socket.gethostname()
print socket.gethostbyname(socket.gethostname())
print "============================================"

for host in [ 'kyi77', 'www', 'www.python.org', 'nosuchname' ]:
    try:
        print '%s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%s : %s' % (host, msg)
print "============================================"

"""
For access to more naming information about a server, use the function
gethostbyname_ex() . It returns the canonical hostname of the server, any aliases,
and all the available IP addresses that can be used to reach it.
"""
for host in [ 'kyi77', 'www', 'www.python.org', 'nosuchname' ]:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print ' Hostname:', hostname
        print ' Aliases :', aliases
        print ' Addresses:', addresses
    except socket.error as msg:
        print 'ERROR:', msg
print "============================================"

"""
When the address of a server is available, use gethostbyaddr() to do a reverse lookup for the name.
"""
hostname, aliases, addresses = socket.gethostbyaddr('127.0.1.1')
print 'Hostname :', hostname
print 'Aliases :', aliases
print 'Addresses:', addresses