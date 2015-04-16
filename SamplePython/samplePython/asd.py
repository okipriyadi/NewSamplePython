import ssl
import socket
 
s_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = ssl.wrap_socket(s_, 
                    ca_certs='/usr/local/lib/python2.7/dist-packages/requests/cacert.pem', 
                    cert_reqs=ssl.CERT_REQUIRED)
 
s.connect(('www.google.com', 443))
 
# s.cipher() - Returns a tuple: ('RC4-SHA', 'TLSv1/SSLv3', 128)
# s.getpeercert() - Returns a dictionary: 
#
#   {'notAfter': 'May 15 00:00:00 2014 GMT',
#    'subject': ((('countryName', u'US'),),
#                (('stateOrProvinceName', u'California'),),
#                (('localityName', u'Mountain View'),),
#                (('organizationName', u'Google Inc'),),
#                (('commonName', u'www.google.com'),)),
#    'subjectAltName': (('DNS', 'www.google.com'),)}
 
s.write("""GET / HTTP/1.1\r Host: www.google.com\r\n\r\n""")
 
# Read the first part (might require multiple reads depending on size and 
# encoding).
d = s.read()
print d
s.close()