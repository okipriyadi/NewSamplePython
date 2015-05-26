import os.path
for path in [ 'one//two//three', 'one/./two/./three', 'one/../alt/two/three', ]:
    print '%20s : %s' % (path, os.path.normpath(path))