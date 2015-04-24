#The number assigned to a transport protocol can be retrieved with getprotobyname() .
#The values for protocol numbers are standardized and defined as constants in socket with the prefix IPPROTO_ .

import socket
def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names. """
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )

protocols = get_constants('IPPROTO_')
for name in [ 'icmp', 'udp', 'tcp' ]:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print '%4s -> %2d (socket.%-12s = %2d)' %(name, proto_num, const_name, getattr(socket, const_name))