"""
To decode the query string, see the FieldStorage class from the cgi module.
Special characters within the query arguments that might cause parse problems
with the URL on the server side are "quoted" when passed to urlencode() . To quote
them locally to make safe versions of the strings, use the quote() or quote_plus()
functions directly.

"""
import urllib
url = 'http://localhost:8080/~dhellmann/'
print 'urlencode() :', urllib.urlencode({'url':url})
print 'quote() :', urllib.quote(url)
print 'quote_plus():', urllib.quote_plus(url)

#To reverse the quote operations, use unquote() or unquote_plus() , as appropriate.
print urllib.unquote('http%3A//localhost%3A8080/%7Edhellmann/')
print urllib.unquote_plus('http%3A%2F%2Flocalhost%3A8080%2F%7Edhellmann%2F')