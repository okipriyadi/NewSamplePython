"""
There are several ways to assemble the parts of a split URL back together into a single
string. The parsed URL object has a geturl() method.
geturl() only works on the object returned by urlparse() or urlsplit() .
"""
from urlparse import urlparse
original = 'http://netloc/path;param?query=arg#frag'
print 'original :', original
parsed = urlparse(original)
print "parsed = ", parsed 
print 'unparsed =', parsed.geturl()

print "============================================"
"""
A regular tuple containing strings can be combined into a URL with urlun- parse() .
While the ParseResult returned by urlparse() can be used as a tuple, 
this example explicitly creates a new tuple to show that urlunparse() works with normaltuples, too.
"""
from urlparse import urlunparse
original = 'http://netloc/path;param?query=arg#frag'
print 'original :', original
parsed = urlparse(original)
print 'type parsed:', type(parsed)
print 'parse :', parsed
t = parsed[:]
print 'Type :', type(t)
print 't : ', t
print 'new :', urlunparse(t)

print "============================================"
"""
If the input URL included superfluous(tak berguna) parts, those may be dropped from the
reconstructed URL. In this case, parameters, query, and fragment are all missing in the original URL.
The new URL does not look the same as the original, but it is equivalent according to the standard.
"""
original = 'http://netloc/path;?#'
print 'ORIG :', original
parsed = urlparse(original)
print 'PARSED:', type(parsed), parsed
t = parsed[:]
print 'TUPLE :', type(t), t
print 'NEW:', urlunparse(t)