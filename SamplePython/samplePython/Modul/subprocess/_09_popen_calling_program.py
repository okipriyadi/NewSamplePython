import subprocess
print 'write:'
proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE,)
proc.communicate('\tstdin: to stdin\n')