"""
Besides working with paths, os.path includes functions for retrieving file properties,
similar to the ones returned by os.stat()

os.path.getatime() returns the access time, os.path.getmtime() ret-
urns the modification time, and os.path.getctime() returns the creation time.
os.path.getsize() returns the amount of data in the file, represented in bytes.
"""

import os.path
import time
print 'File :', __file__ 
print 'Access time :', time.ctime(os.path.getatime(__file__))
print 'Modified time:', time.ctime(os.path.getmtime(__file__))
print 'Change time :', time.ctime(os.path.getctime(__file__))
print 'Size :', os.path.getsize(__file__)




