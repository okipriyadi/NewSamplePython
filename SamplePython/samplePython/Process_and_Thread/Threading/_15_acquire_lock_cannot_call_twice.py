"""
Normal Lock objects cannot be acquired more than once, even by the same thread. This
limitation can introduce undesirable side effects if a lock is accessed by more than one
function in the same call chain.
In this case, the second call to acquire() is given a zero timeout to prevent it
from blocking because the lock has been obtained by the first call.
"""

import threading
lock = threading.Lock()
print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)
print 'third try:', lock.acquire()
print 'forth try:', lock.acquire(0)
