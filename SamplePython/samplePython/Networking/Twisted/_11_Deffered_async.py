import sys
from twisted.internet import reactor
from twisted.internet.defer import Deferred

def got_poem(poem):
    print poem
    reactor.stop()

def poem_failed(err):
    print >>sys.stderr, 'poem download failed'
    print >>sys.stderr, 'I am terribly sorry'
    print >>sys.stderr, 'try again later?'
    reactor.stop()


d = Deferred()
d.addCallbacks(got_poem, poem_failed)
reactor.callWhenRunning(d.callback, 'Another short poem.')
reactor.run()
