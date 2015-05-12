"""
sys contains attributes and functions for accessing compile-time or runtime configura-
tion settings for the interpreter.
Build-Time Version Information
The version used to build the C interpreter is available in a few forms. sys.version is
a human-readable string that usually includes the full version number, as well as infor-
mation about the build date, compiler, and platform. sys.hexversion is easier to use
for checking the interpreter version since it is a simple integer. When formatted using
hex() , it is clear that parts of sys.hexversion come from the version information
also visible in the more readable sys.version_info (a five-part tuple representing
just the version number).
More specific information about the source that went into the build can be found
in the sys.subversion tuple, which includes the actual branch and subversion revi-
sion that was checked out and built. The separate C API version used by the current
interpreter is saved in sys.api_version .
"""
import sys
print 'Version info:'
print 'sys.version' ,repr(sys.version)
print 'sys.version_info', sys.version_info
print 'sys.hexversion', hex(sys.hexversion) 
print 'sys.subversion', sys.subversion
print 'sys.api_version', sys.api_version




#All the values depend on the actual interpreter used to run the sample program.