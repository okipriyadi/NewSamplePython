"""
Creating temporary files with unique names securely, so they cannot be guessed
by someone wanting to break the application or steal the data

TemporaryFile() opens and returns an unnamed file,
NamedTemporaryFile() opens and returns a named file, and mkdtemp() creates
a temporary directory and returns its name.

Applications that need temporary files to store data, without needing to share those files
with other programs, should use the TemporaryFile() function to create the files.

This makes it impossible for another program to find or open the file, since there is
no reference to it in the file system table. The file created by TemporaryFile() is
removed automatically when it is closed, whether by calling close() or by using the
context manager API and with statement.
"""
import time
import os
import tempfile

print '========================Building a filename with PID:'
filename = '/tmp/guess_my_name.%s.txt' % os.getpid()
temp = open(filename, 'w+b')
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
    time.sleep(5)
finally:
    temp.close()
    # Clean up the temporary file yourself
    os.remove(filename)

print '=======================TemporaryFile:'
temp = tempfile.TemporaryFile()
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
    time.sleep(6)
finally:
    # Automatically cleans up the file
    temp.close()