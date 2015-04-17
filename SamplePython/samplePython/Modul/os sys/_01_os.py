import os.path



"""
os.sep= misal "/"
os.extsep = menghasilkan separator antara text dan extensi misal (.)
os.pardir = parent direktory naik satu folder ke atas)
os.curdir = current direktory
"""

"""
The split() function breaks the path into two separate parts and returns a tuple
with the results. The second element of the tuple is the last component of the path,
and the first element is everything that comes before it.
""" 
print "===================== os.path.split ====================="
for path in [ '/one/two/three', '/one/two/three/','/','.','']:
    print '%15s : %s' % (path, os.path.split(path))

"""
The basename() function returns a value equivalent to the second part of the
split() value.
"""

print "===================== os.path.basename ====================="
for path in [ '/one/two/three', '/one/two/three/', '/', '.', '']:
    print '%15s : %s' % (path, os.path.basename(path))
    
print "===================== os.path.dirame ====================="
for path in [ '/one/two/three', '/one/two/three/', '/', '.', '']:
    print '%15s : %s' % (path, os.path.dirname(path))
    
"""
splitext() works like split() , but divides the path on the extension separator,
rather than the directory separator.
"""

print "===================== os.path.splitext ====================="
for path in [ 'filename.txt', 'filename', '/path/to/filename.txt', '/', '', 'my-archive.tar.gz', 'no-extension.', ]:
    print '%21s :' % path, os.path.splitext(path)
    
"""
commonprefix() takes a list of paths as an argument and returns a single string
that represents a common prefix present in all paths. The value may represent a path
that does not actually exist, and the path separator is not included in the consideration,
so the prefix might not stop on a separator boundary.
"""
print "===================== os.path.commonprefix ====================="
paths = ['/one/two/three/four', '/one/two/threefold', '/one/two/three/', ]
for path in paths:
    print 'PATH:', path
    print
    print 'PREFIX:', os.path.commonprefix(paths)
    

"""
Combining Path os.path.join
If any argument to join begins with os.sep , all previous arguments are discarded
and the new one becomes the beginning of the return value.
"""
print "===================== os.path.join ====================="
for parts in [ ('one', 'two', 'three'), ('/', 'one', 'two', 'three'), ('/one', '/two', '/three'),]:
    print parts, ':', os.path.join
    
"""
It is also possible to work with paths that include variable components that can be expanded automatically. 
For example, expanduser() converts the tilde ( ~ ) char-acter to the name of a user's home directory.
If the user's home directory cannot be found, the string is returned unchanged, as
with ~postgresql in this example.
"""
print "===================== os.path.expanduser ====================="
for user in [ '', 'kyi', 'postgresql' ]:
    lookup = '~' + user
    print '%12s : %s' % (lookup, os.path.expanduser(lookup))
"""
expandvars() is more general, and expands any shell environment variables present in the path.
"""
print "===================== os.path.expandvars ====================="
os.environ['MYVAR'] = 'VALUE'
print os.path.expandvars('/path/to/$MYVAR')

