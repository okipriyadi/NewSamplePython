from datetime import datetime
from twisted.internet.task import LoopingCall
from twisted.internet import reactor

def hyper_task():
    print "I like to run fast", datetime.now()

def tired_task():
    print "I want to run slowly", datetime.now()

lc = LoopingCall(hyper_task)
lc.start(0.1)

lc2 = LoopingCall(tired_task)
lc2.start(0.5)

reactor.run()