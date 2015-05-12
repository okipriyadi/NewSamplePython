"""
the process management examples for the os module include a demonstration of
signaling between processes using os.fork() and os.kill() . Since each Popen
instance provides a pid attribute with the process id of the child process, it is possible to
do something similar with subprocess . The next example combines two scripts. This
child process sets up a signal handler for the USR signal.
"""

import os
import signal
import time
import sys

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received = True
    print 'CHILD %6s: Received USR1' % pid
    sys.stdout.flush()

print 'CHILD %6s: Setting up signal handler' % pid
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)

print 'CHILD %6s: Pausing to wait for signal' % pid
sys.stdout.flush()
time.sleep(6)

if not received:
    print 'CHILD %6s: Never received signal' % pid