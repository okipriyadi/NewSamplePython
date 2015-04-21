"""
if an explicit destination is not given using the dir argument, the path used for the
temporary files will vary based on the current platform and settings. The tempfile
module includes two functions for querying the settings being used at runtime.

The value returned by gettempdir() is set based on a straightforward algorithm
of looking through five locations for the first place the current process can create a file.
This is the search list.
1.The environment variable TMPDIR
2. The environment variable TEMP
3. The environment variable TMP
4. A fallback, based on the platform. (RiscOS uses Wimp$ScrapDir . Windows
uses the first available of C:\TEMP , C:\TMP , \TEMP , or \TMP . Other platforms
use /tmp , /var/tmp , or /usr/tmp .)
5. If no other directory can be found, the current working directory is used.
"""

import tempfile
print 'gettempdir():', tempfile.gettempdir()
print 'gettempprefix():', tempfile.gettempprefix()
"""
Programs that need to use a global location for all temporary files without using
any of these environment variables should set tempfile.tempdir directly by assign-
ing a value to the variable.
"""

tempfile.tempdir = '/I/changed/this/path'
print 'gettempdir():', tempfile.gettempdir()