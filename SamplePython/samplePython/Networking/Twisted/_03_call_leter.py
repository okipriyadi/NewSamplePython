"""
reactor.callLater(waktu, callback)
 With callLater the callback is the second argument and the first argument is the number of seconds in the future you would like your callback to run. You can use a floating point number to specify a fractional number of seconds, too.
"""

class Countdown(object):
 
    counter = 5
 
    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)
 
from twisted.internet import reactor
 
reactor.callWhenRunning(Countdown().count)
 
print 'Start!'
reactor.run()
print 'Stop!'