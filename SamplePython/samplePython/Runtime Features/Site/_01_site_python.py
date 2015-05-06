"""
The site module handles site-specific configuration, especially the import path.
site is automatically imported each time the interpreter starts up. On import, it
extends sys.path with site-specific names constructed by combining the prefix val-
ues sys.prefix and sys.exec_prefix with several suffixes. The prefix values used
are saved in the module-level variable PREFIXES for reference later. Under Windows,
the suffixes are an empty string and lib/site-packages . For UNIX-like plat-
forms, the values are lib/python$version/site-packages (where $version is
replaced by the major and minor version number of the interpreter, such as 2.7 ) and
lib/site-python .
"""

import sys
import os
import platform
import site

if 'Windows' in platform.platform():
    SUFFIXES = [ '', 'lib/site-packages',]
else:
    SUFFIXES = ['lib/python%s/site-packages' % sys.version[:3], 'lib/site-python', ]

print 'Path prefixes:'

for p in site.PREFIXES:
    print ' ', p
    
for prefix in sorted(set(site.PREFIXES)):
    print
    print prefix

for suffix in SUFFIXES:
    print
    print ' ', suffix
    path = os.path.join(prefix, suffix).rstrip(os.sep)
    print 'exists :', os.path.exists(path)
    print 'in path:', path in sys.path
