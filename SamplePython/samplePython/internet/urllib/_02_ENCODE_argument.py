"""
Arguments can be passed to the server by encoding them and appending them to the
URL.
"""

import urllib
query_args = { 'q':'query string', 'foo':'bar' }
encoded_args = urllib.urlencode(query_args)
print 'Encoded:', encoded_args
url = 'http://localhost:8080/?' + encoded_args
print 'url =',url
print 'urlopen = ', urllib.urlopen(url).read()