"""
The wait() method takes an argument representing the number of seconds to
wait for the event before timing out. It returns a Boolean indicating whether or not the
event is set, so the caller knows why wait() returned. The isSet() method can be
used separately on the event without fear of blocking.
In this example, wait_for_event_timeout() checks the event status without
blocking indefinitely. The wait_for_event() blocks on the call to wait() , which
does not return until the event status changes.
"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s', )

def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    event_is_set = e.wait()
    logging.debug('event set: %s', event_is_set)

def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    while not e.isSet():
        logging.debug('wait_for_event_timeout starting')
        event_is_set = e.wait(t)
        logging.debug('event set: %s', event_is_set)
    if event_is_set:
        logging.debug('processing event')
    else:
        logging.debug('doing other work')
        
e = threading.Event()
t1 = threading.Thread(name='block',target=wait_for_event, args=(e,))
t1.start()

t2 = threading.Thread(name='nonblock',target=wait_for_event_timeout,args=(e, 2))
t2.start()
logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')