"""
The os module provides several functions for managing the I/O of child processes using
pipes. The functions all work essentially the same way, but return different file handles
depending on the type of input or output desired. For the most part, these functions are
made obsolete by the subprocess module (added in Python 2.4), but it is likely that
legacy code uses them.
The most commonly used pipe function is popen() . It creates a new process
running the command given and attaches a single stream to the input or output of that
process, depending on the mode argument.

The descriptions of the streams also assume UNIX-like terminology.
- stdin The "standard input" stream for a process (file descriptor 0) is readable
by the process. This is usually where terminal input goes.
- stdout The "standard output" stream for a process (file descriptor 1) is writable
by the process and is used for displaying regular output to the user.
- stderr The "standard error" stream for a process (file descriptor 2) is writable
by the process and is used for conveying error messages.
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