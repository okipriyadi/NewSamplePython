"""
As you probably know, a Python generator is a "restartable function" that you create by using the yield expression 
in the body of your function. By doing so, the function becomes a "generator function" that returns an 
iterator you can use to run the function in a series of steps. Each cycle of the iterator restarts 
the function, which proceeds to execute until it reaches the next yield.
"""


def my_generator():
    print 'starting up'
    yield 1
    print "workin'"
    yield 2
    print "still workin'"
    yield 3
    print 'done'

for n in my_generator():
    print "for ke -",n
