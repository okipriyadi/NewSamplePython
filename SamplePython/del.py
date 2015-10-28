"""
callLater akan dieksekusi tepat setelah jangka waktu yang diberikan pada parameter pertama dalam contoh ini 1 detik       

 With callLater the callback is the second argument and the first argument is the number of seconds in the future you would like your callback to run. You can use a floating point number to specify a fractional number of seconds, too.

 And Twisted uses timeouts to make sure any "timed callbacks" registered with callLater get called at the right time. Or rather, at approximately the right time. If another callback takes a really long time to execute, a timed callback may be delayed past its schedule.
"""
from twisted.internet import reactor

status = 1
def stop2():
    print "stop", status
    
    if status == 0:
        print "why"
        reactor.stop()

class Countdown(object):
 
    counter = 5
    def count(self):
        global status 
        status = 9
        print "count status," , status
        if self.counter == 0:
            status = 0
            reactor.callLater(1, stop2)
            #reactor.stop()
            pass
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)
 
 
reactor.callWhenRunning(Countdown().count)
reactor.callLater(4, Countdown().count)
reactor.callLater(7, Countdown().count)
reactor.callLater(9, Countdown().count)
 
print 'Start!'
reactor.run()
print 'Stop!'