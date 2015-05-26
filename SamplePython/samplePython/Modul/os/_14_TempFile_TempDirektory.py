"""
When several temporary files are needed, it may be more convenient to create a single
temporary directory with mkdtemp() and open all the files in that directory.

Since the directory is not 'opened' per se, it must be removed explicitly when it is
no longer needed.
"""


import os
import tempfile
import time
directory_name = tempfile.mkdtemp()
print directory_name
time.sleep(8)
# Clean up the directory
os.removedirs(directory_name)