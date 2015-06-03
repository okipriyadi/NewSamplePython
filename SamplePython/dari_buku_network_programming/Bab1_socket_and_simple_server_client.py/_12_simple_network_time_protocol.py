"""
Unlike the previous recipe, sometimes, you don't need to get the precise time from the NTP
server. You can use a simpler version of NTP called simple network time protocol.

Let us create a plain SNTP client without using any third-party library.
Let us first define two constants: NTP_SERVER and TIME1970. NTP_SERVER is the server
address to which our client will connect, and TIME1970 is the reference time on January 1,
1970 (also called Epoch). You may find the value of the Epoch time or convert to the Epoch
time at http://www.epochconverter.com/ . The actual client creates a UDP socket
( SOCK_DGRAM ) to connect to the server following the UDP protocol. The client then needs to
send the SNTP protocol data ( '\x1b' + 47 * '\0' ) in a packet. Our UDP client sends and
receives data using the sendto() and recvfrom() methods.
"""

import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data, (NTP_SERVER, 123))
    data, address = client.recvfrom( 1024 )
    if data:
        print 'Response received from:', address
        t = struct.unpack( '!12I', data )[10]
        t -= TIME1970
        print '\tTime=%s' % time.ctime(t)

if __name__ == '__main__':
    sntp_client()
