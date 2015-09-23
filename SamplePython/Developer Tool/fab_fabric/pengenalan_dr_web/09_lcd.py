"""
lcd (fabric.context_managers.lcd)

The lcd context manager (local cd) works very similarly to one above (cd); 
however, it only affects the local system's state.

Usage examples:
"""
from fabric.api import lcd, put
# Change the local working directory to project's
# and upload a tar archive
with lcd("/home/kyi/Dropbox"):
    print "Uploading the project archive"
    put("mdcs.db", "~/mdcs4.odt")