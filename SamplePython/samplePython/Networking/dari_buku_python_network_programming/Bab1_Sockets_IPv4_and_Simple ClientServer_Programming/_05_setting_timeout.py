"""
Sometimes, you need to manipulate the default values of certain properties of a socket
library, for example, the socket timeout.

How to do it...
You can make an INSTANCE of a socket object and call a gettimeout() method to get the
default timeout value and the settimeout() method to set a specific timeout value. 
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Default socket timeout: %s" %s.gettimeout()

s.settimeout(100)
print "Current socket timeout: %s" %s.gettimeout()


