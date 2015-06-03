def foo(*args):
    for a in args:
        print a
        
foo(1)

print "\nbanyak Argument(args) :"
foo(1,2,3)

def bar(**kwargs):
   for a in kwargs:
        print a, kwargs[a]
        
print "\nbanyak Argument(kwargs) :"
bar(name="one", age=27)

"""
Both idioms can be mixed with normal arguments to allow a set of fixed and 
some variable arguments:
"""
def foo(kind, *args, **kwargs):
   pass


print "\n An other usage of the *l idiom is to unpack argument lists when calling a function"
def foo(bar, lee):
    print bar, lee
    
l = [1,2]
foo(*l)   
