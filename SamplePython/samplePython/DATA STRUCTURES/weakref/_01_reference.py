"""
Refer to an "expensive" object, but allow its memory to be
reclaimed by the garbage collector if there are no other nonweak references.
The weakref module supports weak references to objects. A normal reference increments the 
reference count on the object and prevents it from being garbage collected.
This is not always desirable, either when a circular reference might be present or when
building a cache of objects that should be deleted when memory is needed. A weak
reference is a handle to an object that does not keep it from being cleaned up automati-
cally.
"""

import weakref

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

obj = ExpensiveObject()
r = weakref.ref(obj)

print 'obj:', obj
print 'ref:', r
print 'r():', r()

print 'deleting obj'
del obj
print 'r():', r()
