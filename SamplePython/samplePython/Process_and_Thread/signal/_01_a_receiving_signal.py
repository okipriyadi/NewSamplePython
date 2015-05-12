"""
As with other forms of event-based programming, signals are received by establishing
a callback function, called a signal handler, that is invoked when the signal occurs.
The arguments to the signal handler are the signal number and the stack frame from the
point in the program that was interrupted by the signal.

This example script loops indefinitely, pausing for a few seconds each time.
When a signal comes in, the sleep() call is interrupted and the signal handler
receive_signal() prints the signal number. After the signal handler returns, the
loop continues.
Send signals to the running program using os.kill() or the UNIX command line program kill.

$ kill -USR1 $pid
$ kill -USR2 $pid
$ kill -INT $pid contoh jika program ini berjalan di PID 5361 maka untuk mematikannya dengan cara
kill -INT 5361
"""

import signal
import os
import time

def receive_signal(signum, stack):
    print 'Received:', signum

# Register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)
# Print the process ID so it can be used with 'kill'
# to send this program signals.
print 'My PID is:', os.getpid()
while True:
    print 'Waiting...'
    time.sleep(3)