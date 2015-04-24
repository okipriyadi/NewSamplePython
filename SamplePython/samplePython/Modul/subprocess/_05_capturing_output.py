"""
The standard input and output channels for the process started by call() are bound to
the parent's input and output. That means the calling program cannot capture the output
of the command. Use check_output() to capture the output for later processing.
"""

import subprocess
output = subprocess.check_output(['ls', '-1'])
print 'Have %d bytes in output' % len(output)
print output
print "type output", type(output)