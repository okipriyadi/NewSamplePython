"""
The functions call() , check_call() , and check_output() are wrappers around
the Popen class. Using Popen directly gives more control over how the command
is run and how its input and output streams are processed. For example, by passing
different arguments for stdin, stdout, and stderr, it is possible to mimic the variations
of os.popen() .
"""

"""
One-Way Communication with a Process
To run a process and read all its output, set the stdout value to PIPE and call
communicate() .
"""
import subprocess
print 'read'
proc= subprocess.Popen(['echo','"to_stdout"'], stdout=subprocess.PIPE,)
stdout_value = proc.communicate()[0]
print "stdout :", stdout_value
