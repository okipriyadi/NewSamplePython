"""
Signals and threads do not generally mix well because only the main thread of a process
will receive signals. The following example sets up a signal handler, waits for the signal
in one thread, and sends the signal from another thread.

signal hanler diregistrasi di thread utama karena python requierment untuk modul signal memang mengharuskan
sepert itu. regardless of underlying platform support for mixing threads and signals. 
Although the receiver thread calls signal.pause() , it does not receive the signal. 
The signal.alarm(2) call near the end of the example prevents an infinite block, 
since the receiver thread will never exit.
"""

import signal
import threading 
import os
import time

def signal_handler(num, stack):
    print 'Received signal %d in %s' % (num, threading.currentThread().name)

signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print 'Waiting for signal in', threading.currentThread().name
    signal.pause()
    print 'Done waiting'


# Start a thread that will not receive the signal
receiver = threading.Thread(target=wait_for_signal, name='receiver')
receiver.start()
time.sleep(0.1)

def send_signal():
    print 'Sending signal in', threading.currentThread().name
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# Wait for the thread to see the signal (not going to happen!)
print 'Waiting for', receiver.name
signal.alarm(2)
receiver.join()