"""
Decorators provide a simple syntax for calling higher-order functions. 
By definition, a decorator is a function that takes another function and 
extends the behavior of the latter function without explicitly modifying it. 

Sounds confusing but it's really not, especially after we go over a number of examples.
"""

"""
===================================================
First things first
===================================================
Essentially, functions return a value based on the given arguments.
"""
def foo(bar):
  return bar + 1

print foo(2)
print foo(2) == 3

"""
===================================================
First class object
===================================================
In Python, functions are first-class objects. This means that functions can be passed around,
and used as arguments, just like any other value (e.g, string, int, float).
"""
print "=====================First class object====================="
print foo
print foo(2)
print type(foo)

def call_foo_with_arg(foo, arg):
  return foo(arg)

print call_foo_with_arg(foo, 3)

"""
===================================================
Nested Functions
===================================================
Because of the first-class nature of functions in Python, you can define functions inside 
other functions. Such functions are called nested functions.
"""

print "=====================Nested Function====================="
def parent():
  print "Printing from the parent() function."

  def first_child():
      return "Printing from the first_child() function."

  def second_child():
      return "Printing from the second_child() function."

  print first_child()
  print second_child()
  return "finished"
  
print parent()

"""
Whenever you call parent(), the sibling functions, first_child() and second_child() are also called AND because of scope, both of the sibling functions are not available (e.g., cannot be called) outside of the parent function.
"""

"""
===================================================
Example 1
===================================================
"""
print "=====================Example 1====================="
def my_decorator(some_function):

  def wrapper():

      print "Something is happening before some_function() is called."

      some_function()

      print "Something is happening after some_function() is called."

  return wrapper

def just_some_function():
  print "Wheee!"


just_some_function = my_decorator(just_some_function)
just_some_function()

#To understand what's going on here, just look back at the four previous examples. We are literally just applying everything learned. Put simply, decorators wrap a function, modifying its behavior. L et's take it one step further and add an if statement.

"""
===================================================
Example 2
===================================================
"""
print "=====================Example 2====================="
def my_decorator(some_function):

  def wrapper():

      num = 10

      if num == 10:
          print "Yes!"
      else:
          print "No!"

      some_function()

      print "Something is happening after some_function() is called."

  return wrapper

def just_some_function():
 print "Wheee!"

just_some_function = my_decorator(just_some_function)
just_some_function()


"""
===================================================
Let's create a module for our decorator:
===================================================
"""
print "=====================decorator====================="
def my_decorator(some_function):

  def wrapper():

      num = 10

      if num == 10:
          print "Yes!"
      else:
          print "No!"

      some_function()

      print "Something is happening after some_function() is called."

  return wrapper

if __name__ == "__main__":
  my_decorator()