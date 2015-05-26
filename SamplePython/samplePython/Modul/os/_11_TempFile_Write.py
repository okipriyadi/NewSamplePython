"""
By default, the file handle is created with mode ’w+b’ so it behaves consistently
on all platforms, and the caller can write to it and read from it.

After writing, the file handle must be “rewound” using seek() in order to read
the data back from it.
"""

import os
import tempfile
with tempfile.TemporaryFile() as temp:
    temp.write('Some data')
    temp.seek(0)
    print temp.read()