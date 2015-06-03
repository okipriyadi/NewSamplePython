"""
port numbers for network services with standardized names can be looked up using getservbyname() .
To reverse the service port lookup, use getservbyport().

socket class = for handling the actual data channel, and also includes functions for network-related tasks, 
such as converting a servers name to an address and formatting data to be sent across the network
"""

import socket

"""socket.gethostname() = Return a string containing the hostname \
of the machine where the Python interpreter is currently executing."""
print "socket.gethostname() =", socket.gethostname() 

"""socket.gethostbyname(hostname) = socket.gethostbyname(hostname)
Translate a host name to IPv4 address format."""
print "socket.gethostbyname(hostname) = ", socket.gethostbyname(socket.gethostname())
try:
    print "socket.gethostbyname(www.google.com) = ", socket.gethostbyname("http://git.palocal.net")
except socket.error as msg:
    print 'ERROR:', msg
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