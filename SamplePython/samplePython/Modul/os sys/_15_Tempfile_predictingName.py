"""
While less secure than strictly anonymous temporary files, including a predictable por-
tion in the name makes it possible to find the file and examine it for debugging pur-
poses. All functions described so far take three arguments to control the filenames to
some degree. Names are generated using the following formula.

dir + prefix + random + suffix
All values except random can be passed as arguments to TemporaryFile() ,
NamedTemporaryFile() , and mkdtemp() . For example:
"""

import tempfile
with tempfile.NamedTemporaryFile(suffix='_suffix', prefix='prefix_', dir='/tmp',) as temp:
    print 'temp:', temp
    print 'temp.name:', temp.name