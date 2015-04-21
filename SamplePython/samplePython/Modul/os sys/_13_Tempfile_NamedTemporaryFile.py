"""
There are situations where having a named temporary file is important. For applica-
tions spanning multiple processes, or even hosts, naming the file is the simplest way
to pass it between parts of the application. The NamedTemporaryFile() function
creates a file without unlinking it, so the file retains its name (accessed with the name
attribute)
"""
import os
import tempfile
import time
with tempfile.NamedTemporaryFile() as temp:
    print 'temp:', temp
    print 'temp.name:', temp.name
    time.sleep(6)
    print 'Exists after close:', os.path.exists(temp.name)