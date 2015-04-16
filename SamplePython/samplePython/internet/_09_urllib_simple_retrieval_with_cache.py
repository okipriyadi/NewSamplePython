"""
Purpose Accessing remote resources that do not need authentication,
cookies, etc.

The urllib module provides a simple interface for network resource access. It also
includes functions for encoding and quoting arguments to be passed over HTTP to a
server.

Downloading data is a common operation, and urllib includes the urlretrieve() function to meet this need. 
urlretrieve() takes arguments for the URL, a temporary file to hold the data, 
a function to report on download progress, 
and data to pass if the URL refers to a form where data should be posted. If no filename is given
urlretrieve() creates a temporary file. The calling program can delete the file directly or 
treat the file as a cache and use urlcleanup() to remove it.
"""
import urllib
import os
def reporthook(blocks_read, block_size, total_size):
    """total_size is reported in bytes.
    block_size is the amount read each time.
    blocks_read is the number of blocks successfully read.
    """
    if not blocks_read:
        print 'Connection opened'
        return
    if total_size < 0:
        # Unknown size
        print 'Read %d blocks (%d bytes)' % (blocks_read,blocks_read * block_size)
    else: 
        amount_read = blocks_read * block_size
        print 'Read %d blocks, or %d/%d' % (blocks_read, amount_read, total_size)
    return
filename, msg = urllib.urlretrieve('http://blog.doughellmann.com/', reporthook=reporthook)
"""
print
print 'File:', filename
print 'Headers:'
print msg
print 'File exists before cleanup:', os.path.exists(filename)


urllib.urlcleanup()
print 'File still exists:', os.path.exists(filename)
"""