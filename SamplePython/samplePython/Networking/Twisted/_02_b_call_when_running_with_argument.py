class Countdown(object):
 
    def __init__(self, waktu):
        self.counter = waktu
 
    def count(self):
        if self.counter == 0:
            reactor.stop()
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)
 
from twisted.internet import reactor

reactor.callWhenRunning(Countdown(10).count)
print 'Start!'
reactor.run()
print 'Stop!'