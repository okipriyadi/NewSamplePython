from twisted.internet import reactor

def f():
    print "this will run 3.5 seconds after it was scheduled "

reactor.callLater(3.5, f)

# f() will only be called if the event loop is started.
reactor.run()