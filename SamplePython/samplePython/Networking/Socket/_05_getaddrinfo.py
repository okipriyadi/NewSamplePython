"""
getaddrinfo() takes several arguments for filtering the result list. The host and
port values given in the example are required arguments. The optional arguments are
family, socktype, proto, and flags. The optional values should be either 0 or one of the
constants defined by socket .
"""

import socket
def get_constants(prefix):
    """Create a dictionary mapping socket module
    constants to their names.
    """
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')
for response in socket.getaddrinfo('www.doughellmann.com', 'http',
                                   socket.AF_INET, # family
                                   socket.SOCK_STREAM, # socktype
                                   socket.IPPROTO_TCP, # protocol
                                   socket.AI_CANONNAME, # flags
                                   ):
    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response
    print 'Family:',families[family]
    print 'Type:', types[socktype]
    print 'Protocol:', protocols[proto]
    print 'Canonical name:', canonname
    print 'Socket address:', sockaddr 
    print
    
    """
    Since flags includes AI_CANONNAME , the canonical name of the server, which may
    be different from the value used for the lookup if the host has any aliases, is included
    in the results this time. Without the flag, the canonical name value is left empty.
    """