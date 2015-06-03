"""
When you would like to deal with low-level network functions, sometimes, the usual string
notation of IP addresses are not very useful. They need to be converted to the packed 32-bit
binary formats.
The Python socket library has utilities to deal with the various IP address formats. Here,
we will use two of them: inet_aton() and inet_ntoa() .

In this recipe, the two IP addresses have been converted from a string to a 32-bit packed
This helps to represent the binary data in a hexadecimal format.


"""
    
import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print "IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)

if __name__ == '__main__':
    convert_ip4_address()