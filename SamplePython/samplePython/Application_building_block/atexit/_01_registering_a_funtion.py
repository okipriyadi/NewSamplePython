"""
This is an example of registering a function via register() .
"""

import atexit
def all_done():
    print 'all_done()'   

print 'Registering'
atexit.register(all_done)
print 'Registered'