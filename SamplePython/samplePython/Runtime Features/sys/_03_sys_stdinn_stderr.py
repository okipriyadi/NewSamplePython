"""
Following the UNIX paradigm, Python programs can access three file descriptors by
default.

stdin is the standard way to read input, usually from a console but also from
other programs via a pipeline. stdout is the standard way to write output for a user (to
the console) or to be sent to the next program in a pipeline. stderr is intended for use
with warning or error messages"""


import sys
print >>sys.stderr, 'STATUS: Reading from stdin'
data = sys.stdin.read()


print >>sys.stderr, 'STATUS: Writing data to stdout'
sys.stdout.write(data)
sys.stdout.flush()

print >>sys.stderr, 'STATUS: Done'

