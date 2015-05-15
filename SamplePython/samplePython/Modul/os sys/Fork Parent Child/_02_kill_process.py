"""
1. The parent can send signals to the child process using kill() and the signal
 module. First, define a signal handler to be invoked when the signal is received.

2. Then invoke fork() , and in the parent, pause a short amount of time before send-
ing a USR1 signal using kill() . The short pause gives the child process time to set up
the signal handler.

3.In the child, set up the signal handler and go to sleep for a while to give the parent
time to send the signal.
"""
import os
import signal
import time

#define signal handler
def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    pid = os.getpid()   
    print 'Received USR1 in process %s' % pid
    
#forking
print 'Forking...'
child_pid = os.fork()


if child_pid:
    #this is for parent
    print 'PARENT: Pausing before sending signal...'
    time.sleep(1)
    print 'PARENT: Signaling %s' % child_pid
    os.kill(child_pid, signal.SIGUSR1)
else:
    #this is for child
    print 'CHILD: Setting up signal handler'
    signal.signal(signal.SIGUSR1, signal_usr1)
    print 'CHILD: Pausing to wait for signal'
    time.sleep(5)