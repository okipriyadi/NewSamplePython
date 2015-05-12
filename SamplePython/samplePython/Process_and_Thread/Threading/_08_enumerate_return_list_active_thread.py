"""
It is not necessary to retain an explicit handle to all the daemon threads to ensure they
have completed before exiting the main process. enumerate() returns a list of active
Thread instances. The list includes the current thread, and since joining the current
thread introduces a deadlock situation, it must be skipped.

Because the worker is sleeping for a random amount of time, the output from this
program may vary.
"""
import random
import threading
import time
import logging      

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def worker():
    """thread worker function"""
    t = threading.currentThread()
    pause = random.randint(1,5)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('ending')
    return

for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()