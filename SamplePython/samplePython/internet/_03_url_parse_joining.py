"""
In addition to parsing URLs, urlparse includes urljoin() for constructing absolute
URLs from relative fragments.
"""
from urlparse import urljoin
#absolute url
print urljoin('http://www.example.com/path/file.html','anotherfile.html')
print urljoin('http://www.example.com/path/file.html','../anotherfile.html')
#relative url
print urljoin('http://www.example.com/path/', '/subpath/file.html')
print urljoin('http://www.example.com/path/', 'subpath/file.html')