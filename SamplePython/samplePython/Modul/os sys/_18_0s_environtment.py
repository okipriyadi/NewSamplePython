"""
Variables set in the environment are visible as strings that can be read
through os.environ or getenv() . Environment variables are commonly used for
configuration values, such as search paths, file locations, and debug flags. This example
shows how to retrieve an environment variable and pass a value through to a child
process.
"""
import os
print 'Initial value:', os.environ.get('TESTVAR', None)
print 'Child process:'

os.system('echo $TESTVAR')
os.environ['TESTVAR'] = 'THIS VALUE WAS CHANGED'
print

print 'Changed value:', os.environ['TESTVAR']
print 'Child process:'
os.system('echo $TESTVAR')
del os.environ['TESTVAR']
print

print 'Removed value:', os.environ.get('TESTVAR', None)
print 'Child process:'
os.system('echo $TESTVAR')