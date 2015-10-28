"""
deferred will not let us fire the normal result callbacks a second time. In fact, a deferred cannot be fired a second time no matter what, as demonstrated by these examples:
Notice those final print statements are never called. The callback and errback methods are raising genuine Exceptions to let us know we've already fired that deferred
"""

from twisted.internet.defer import Deferred
def out(s): print s

d = Deferred()
d.addCallbacks(out, out)
d.callback('First result')
d.callback('Second result')
print 'Finished'
