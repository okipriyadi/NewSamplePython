"""
The standard dictionary includes the method setdefault() for retrieving a value and
establishing a default if the value does not exist. By contrast, defaultdict lets the
caller specify the default up front when the container is initialized.
"""

import collections
def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print 'd:', d
print 'foo =>', d['foo']
print 'bar =>', d['bar']