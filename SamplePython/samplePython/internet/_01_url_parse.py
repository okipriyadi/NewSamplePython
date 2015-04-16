"""
The urlparse module manipulates URL strings, splitting and combining their components.
There are two client-side APIs for accessing web resources. 
1. urllib
2. urllib2 
urllib2 is easier to extend with new protocols and the urllib2. 
Request provides a way to add custom headers to outgoing requests.

HTTP POST requests are usually 'form encoded' with urllib . Binary data sent
through a POST should be encoded with base64 first, to comply with the message format standard.

To create a custom web server with Python, without requiring any external frame-
works, use BaseHTTPServer as a starting point. It handles the HTTP protocol, so
the only customization needed is the application code for responding to the incoming
requests.
Session state in the server can be managed through cookies created and parsed by
the Cookie module. Full support for expiration, path, domain, and other cookie settings
makes it easy to configure the session.

The uuid module is used for generating identifiers for resources that need unique
values. UUIDs are good for automatically generating Uniform Resource Name (URN) values, 
where the name of the resource needs to be unique but does not need to convey
any meaning.

Python's standard library includes support for two web-based remote procedure-
call mechanisms. The JavaScript Object Notation (JSON) encoding scheme used in
AJAX communication is implemented in json . It works equally well in the client or the
server. Complete XML-RPC client and server libraries are also included in xmlrpclib
and SimpleXMLRPCServer , respectively.
"""

from urlparse import urlparse
"""
The return value from the urlparse() function is an object that acts like a tuple
with six elements.
"""
url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print "parsed = ", parsed

print "============================================"
url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'
parsed = urlparse(url)
print 'scheme :', parsed.scheme
print 'netloc :', parsed.netloc
print 'path :', parsed.path
print 'params :', parsed.params
print 'query :', parsed.query
print 'fragment:', parsed.fragment
print 'username:', parsed.username
print 'password:', parsed.password
print 'hostname:', parsed.hostname, '(netloc in lowercase)'
print 'port :', parsed.port

print "============================================"
"""
The urlsplit() function is an alternative to urlparse() . It behaves a little
differently because it does not split the parameters from the URL. 
This is useful for URLs following RFC 2396, which supports parameters for each segment of the path.
Since the parameters are not split out, the tuple API will show five elements instead
of six, and there is no params attribute.
"""
from urlparse import urlsplit
url = 'http://user:pwd@NetLoc:80/p1;param/p2;param?query=arg#frag'
parsed = urlsplit(url)
print parsed
print 'scheme :', parsed.scheme
print 'netloc :',parsed.netloc
print 'path:',parsed.path
print 'query :', parsed.query
print 'fragment:', parsed.fragment
print 'username:', parsed.username
print 'password:', parsed.password
print 'hostname:', parsed.hostname, '(netloc in lowercase)'
print 'port:', parsed.port 

print "============================================"
"""
To simply strip the fragment identifier from a URL, 
such as when finding a base page name from a URL, use urldefrag() .
"""
from urlparse import urldefrag
original = 'http://netloc/path;param?query=arg#frag'
print 'original:', original
url, fragment = urldefrag(original)
print 'url:', url
print 'fragment:', fragment