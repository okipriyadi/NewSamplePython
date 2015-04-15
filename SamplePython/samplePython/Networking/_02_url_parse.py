"""
port numbers for network services with standardized names can be looked up using getservbyname() .
To reverse the service port lookup, use getservbyport() .
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
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)
    
print "========================To reverse the service port lookup, use getservbyport() ."
for port in [ 80, 443, 21, 70, 25, 143, 993, 110, 995 ]:
    print urlparse.urlunparse((socket.getservbyport(port), 'example.com', '/', '', '', ''))
    