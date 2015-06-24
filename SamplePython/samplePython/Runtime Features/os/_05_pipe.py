"""
The os module provides several functions for managing the I/O of child processes using
pipes. The functions all work essentially the same way, but return different file handles
depending on the type of input or output desired. For the most part, these functions are
made obsolete by the subprocess module

The most commonly used pipe function is popen() . It creates a new process
running the command given and attaches a single stream to the input or output of that
process, depending on the mode argument.

Although the popen() functions work on Windows, some of these examples
assume a UNIX-like shell.
"""

import os

print 'popen, read:'
stdout = os.popen('echo "to stdout"', 'r')
try:
    stdout_value = stdout.read()
finally:
    stdout.close()

print '\tstdout:', repr(stdout_value)
print '\npopen, write:'
stdin = os.popen('cat -', 'w')
try:
    stdin.write('\tstdin: to stdin\n')
finally:
    stdin.close()