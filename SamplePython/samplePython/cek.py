from twisted.internet.task import LoopingCall
from twisted.internet import reactor

class Countdown(object):

    loops = 0
    
    def __init__(self, count_to):
        self.counter = count_to
        self.loop_call = LoopingCall(self.count)
    
        Countdown.loops += 1
    
        self._id = Countdown.loops
    
    def start(self, delay):
        self.loop_call.start(delay)
    
    def count(self):
        # if we done with counting
        if not self.counter:
            # decrease loop_calls counter
            Countdown.loops -=1
            # also stop reactor, if no loops left
            if not Countdown.loops:
                reactor.stop()
            # stop current loop call
            self.loop_call.stop()
        elif self.counter:
            print self._id,':', self.counter
            self.counter -= 1


print 'Start!'

Countdown(8).start(1)
Countdown(10).start(0.5)
Countdown(5).start(1.5)

reactor.run()

print 'Stop!'