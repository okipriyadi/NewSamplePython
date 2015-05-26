"""
Operating systems with hierarchical file systems have a concept of the current working
directory the directory on the file system the process uses as the starting location when
files are accessed with relative paths. The current working directory can be retrieved
with getcwd() and changed with chdir() .
os.curdir and os.pardir are used to refer to the current and parent directories
in a portable manner.
"""

import os
print 'Starting:', os.getcwd()
print 'Moving up one:', os.pardir
os.chdir(os.pardir)
print 'After move:', os.getcwd()