"""
reactor.callLater(waktu, callback)
 With callLater the callback is the second argument and the first argument is the number of seconds in the future you would like your callback to run. You can use a floating point number to specify a fractional number of seconds, too.
"""

class Countdown(object):
    banyak = 0
    id = 0
    def __init__(self, waktu):
        self.counter = waktu
        Countdown.banyak += 1
        Countdown.id += 1 
        self.identitas = self.id 
        print 'banyak =', self.banyak
 
    def count(self):
        if self.counter == 0:
            Countdown.banyak -= 1
            print 'task ', self.identitas, 'berhenti'
            print 'hasil banyak =', self.banyak
            if self.banyak == 0 :    
                reactor.callLater(1,reactor.stop)
        else:
            print 'task ', self.identitas ,': ', self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)
 
from twisted.internet import reactor

reactor.callWhenRunning(Countdown(10).count)
reactor.callWhenRunning(Countdown(8).count)
reactor.callWhenRunning(Countdown(5).count)
print 'Start!'
reactor.run()
print 'Stop!'