"""
To set up the Popen instance for reading and writing at the same time, use a combina-
tion of the previous techniques.
"""
import subprocess
print 'popen2:'
proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,)
msg = 'through stdin to stdout'
stdout_value = proc.communicate(msg)[0]
print 'pass through:', repr(stdout_value)