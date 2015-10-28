import sys
from twisted.internet import reactor
from twisted.internet.defer import Deferred

def got_poem(poem):
    print poem

def poem_failed(err):
    print >>sys.stderr, 'poem download failed'
    print >>sys.stderr, 'I am terribly sorry'
    print >>sys.stderr, 'try again later?'

def poem_done(_):
    reactor.stop()

d = Deferred()
d.addCallbacks(got_poem, poem_failed)
d.addBoth(poem_done)
reactor.callWhenRunning(d.callback, 'Another short poem.')

reactor.run()
