"""
Notice the second callback runs after the first, even though we see the traceback from the exception the first raised. And if you comment out the reactor.stop() call, the program will just keep running forever. So the reactor will keep going even when our callbacks fail (though it will report the exception).
"""
from twisted.internet import reactor


def falldown():
    raise Exception('I fall down.')
 
def upagain():
    print 'But I get up again.'
    reactor.stop()
 
 
reactor.callWhenRunning(falldown)
reactor.callWhenRunning(upagain)
 
print 'Starting the reactor.'
reactor.run()