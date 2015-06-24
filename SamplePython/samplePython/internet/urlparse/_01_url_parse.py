"""
urlparse module memaniulasi URL, men-split dan mengkombinasikan komponen2nya.

Urlparse menyediakan fungsi untuk memecah URL menjadi bagian-bagian tertentu yang sesuai 
dengan ketentuan-ketentuan RFC

nilai return dari fungsi urlparse() adalah sebuah objek berupa tuple dengan 6 elemen 
"""

from urlparse import urlparse
url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url)
print "parsed = ", parsed
print "\n============================================"
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
print "using urlsplit=", parsed
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