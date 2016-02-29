from datetime import datetime
from twisted.internet.task import LoopingCall
from twisted.internet import reactor

def hyper_task(daa):
    print "I like to run fast %s"%daa , datetime.now()

def tired_task():
    print "I want to run slowly", datetime.now()

lc = LoopingCall(hyper_task,'daa')
lc.start(0.1)

lc2 = LoopingCall(tired_task)
lc2.start(0.5)

reactor.run()