"""
In this example, deco is a decorator function that “decorates” the foo function. It takes
the foo function, adds some functionality to it and reassigns it back to the foo name.The
"""

@deco
def foo():
    pass

"""
@deco syntax is equivalent to executing this line of code (given that foo is a valid functionobject):

================================
foo = deco(foo)
================================

The following is a simple example where we acknowledge or log the calling of a func-
tion live as it happens:
"""
def log(func):
    def wrappedFunc():
        print "*** %s() called" % func.__name__
        return func()
return wrappedFunc

@log
def foo():
    print "inside foo()"


"""
Now if we execute this code, we get the following output:
++++++++++++++++++++++++++++++++++++++++++++++++++++++
>>> foo()
*** foo() called
inside foo()
++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""