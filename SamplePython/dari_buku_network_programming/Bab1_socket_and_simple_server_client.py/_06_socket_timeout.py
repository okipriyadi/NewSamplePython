"""
Sometimes, you need to manipulate the default values of certain properties of a socket
library, for example, the socket timeout.

You can make an instance of a socket object and call a gettimeout() method to get the
default timeout value and the settimeout() method to set a specific timeout value. This is
very useful in developing custom server applications.

We first create a socket object inside a test_socket_timeout() function. Then, we can
use the getter/setter instance methods to manipulate timeout values.
"""
import socket
def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" %s.gettimeout()
    s.settimeout(10)
    print "Current socket timeout: %s" %s.gettimeout()

if __name__ == '__main__':
    test_socket_timeout() 