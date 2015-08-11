"""
Downloading data is a common operation, and urllib includes the urlretrieve()
function to meet this need. urlretrieve() takes arguments for the URL, a tem-
porary file to hold the data, a function to report on download progress, and data to
pass if the URL refers to a form where data should be posted. If no filename is given,
urlretrieve() creates a temporary file. The calling program can delete the file di-
rectly or treat the file as a cache and use urlcleanup() to remove it.

This example uses an HTTP GET request to retrieve some data from a web server.
Each time data is read from the server, reporthook() is called to report the
download progress. The three arguments are the number of blocks read so far, the size
(in bytes) of the blocks, and the size (in bytes) of the resource being downloaded. When
the server does not return a Content-length header, urlretrieve() does not know
how big the data should be and passes -1 as the total_size argument.
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
        print 'Read %d blocks (%d bytes)' % (blocks_read, blocks_read * block_size)
    else:
        amount_read = blocks_read * block_size
        print 'Read %d blocks, or %d/%d' % (blocks_read, amount_read, total_size)
    return

try:
    filename, msg = urllib.urlretrieve('http://filepi.com/i/sOsGMl9', reporthook=reporthook) #ganti urlnya dengan url yang bisa mendoenload data
    print
    print 'File:', filename
    print 'Headers:'
    print msg
    print 'File exists before cleanup:', os.path.exists(filename)
finally:
    urllib.urlcleanup()
    print 'File still exists:', os.path.exists(filename)
    

    
    