"""
As with urllib , an HTTP GET operation is the simplest use of urllib2 . Pass
the URL to urlopen() to get a 'file-like' handle to the remote data.
"""

import urllib2
"""
The example server accepts the incoming values and formats a plain-text response
to send back. The return value from urlopen() gives access to the headers from the
HTTP server through the info() method and the data for the remote resource via
methods like read() and readlines() .
"""
response = urllib2.urlopen('http://localhost:8080/')
print 'RESPONSE:', response
print 'URL :', response.geturl()
headers = response.info()
print 'DATE :', headers['date']

print 'HEADERS :'
print '---------'
print headers
data = response.read()
print '---------'
print 'LENGTH :', len(data)
print 'DATA:'
print '---------'
print data