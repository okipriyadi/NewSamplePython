"""
Up to this point, the example programs have implicitly waited to exit until all threads
have completed their work. Programs sometimes spawn a thread as a daemon that runs
without blocking the main program from exiting. Using daemon threads is useful for
services where there may not be an easy way to interrupt the thread, or where letting
the thread die in the middle of its work does not lose or corrupt data (for example, a
thread that generates "heartbeats" for a service monitoring tool). To mark a thread as a
daemon, call its setDaemon() method with True . The default is for threads to not be
daemons.

The output does not include the "Exiting " message from the daemon thread,
since all of the non-daemon threads (including the main thread) exit before the daemon
thread wakes up from its two-second sleep.
"""
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
format='(%(threadName)-10s) %(message)s',)

def daemon():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()