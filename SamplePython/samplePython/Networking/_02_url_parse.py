"""
port numbers for network services with standardized names can be looked up using getservbyname() .
To reverse the service port lookup, use getservbyport().

socket class = for handling the actual data channel, and also includes functions for network-related tasks, 
such as converting a server's name to an address and formatting data to be sent across the network.

Sockets have two primary properties controlling the way they send data: 
1. the address family => controls the OSI network layer protocol used, 
2. the socket type => controls the transport layer protocol

Python supports three address families. 
1. AF_INET , is used for IPv4 Internet addressing.
2. AF_INET6 is used for IPv6 Internet addressing.
3. AF_UNIX is the address family for UNIX Domain Sockets (UDS)
"""
import socket
import urlparse
for url in [ 'http://www.python.org',
                'https://www.mybank.com',
                'ftp://prep.ai.mit.edu',
                'gopher://gopher.micro.umn.edu',
                'smtp://mail.example.com',
                'imap://mail.example.com',
                'imaps://mail.example.com',
                'pop3://pop.example.com',
                'pop3s://pop.example.com',
                ]:
    parsed_url = urlparse.urlparse(url)
    print "urlparse.urlparse(url) =", parsed_url
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)
    
print "========================To reverse the service port lookup, use getservbyport() ."
for port in [ 80, 443, 21, 70, 25, 143, 993, 110, 995 ]:
    print urlparse.urlunparse((socket.getservbyport(port), 'example.com', '/', '', '', ''))
    