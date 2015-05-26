"""
The caller can only read from or write to the streams associated with the child
process, which limits their usefulness. The other file descriptors for the child process are
inherited from the parent, so the output of the cat - command in the second example
appears on the console because its standard output file descriptor is the same as the one
used by the parent script.

The other popen() variants provide additional streams, so it is possible to work
with stdin, stdout, and stderr, as needed. For example, popen2() returns a write-only
stream attached to stdin of the child process and a read-only stream attached to its
stdout.

This simplistic example illustrates bidirectional communication. The value written
to stdin is read by cat (because of the '-' argument) and then written back to stdout.
A more complicated process could pass other types of messages back and forth through
the pipe-even serialized objects.
"""

import os
print 'popen2:'
stdin, stdout = os.popen2('cat -')
try:
    stdin.write('through stdin to stdout')
finally:
    stdin.close()
try:
    stdout_value = stdout.read()
finally:
    stdout.close()

print '\tpass through:', repr(stdout_value)