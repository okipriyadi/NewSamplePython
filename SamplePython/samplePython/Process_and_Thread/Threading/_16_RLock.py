"""

In a situation where separate code from the same thread needs to "reacquire" the
lock, use an RLock instead.
The only change to the code from the previous example is substituting RLock
for Lock .
"""

import threading
lock = threading.Lock()
print 'First try :', lock.acquire()
print 'Second try:', lock.acquire(0)