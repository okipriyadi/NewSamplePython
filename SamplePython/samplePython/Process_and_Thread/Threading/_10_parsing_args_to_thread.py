"""
Because the args and kwargs values passed to the Thread constructor are saved
in private variables using names prefixed with '__' , they are not easily accessed from
a subclass. To pass arguments to a custom thread type, redefine the constructor to save
the values in an instance attribute visible from the subclass.
"""
import threading
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

class MyThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group,
                                  target=target,
                                  name=name,
                                  verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return

for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a':'A', 'b':'B'})  
    t.start()