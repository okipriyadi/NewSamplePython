from twisted.internet import reactor

def f():
    print "I'll never run."

reactor.callLater(5, f)

reactor.run()