"""
The output will vary based on the state of the system each time the example is run.
After the fork, two processes are running the same code. For a program to tell
which one it is in, it needs to check the return value of fork() . If the value is 0 , the
current process is the child. If it is not 0 , the program is running in the parent process
and the return value is the process id of the child process.
"""

import os
pid = os.fork()
if pid:
    print 'Child process id:', pid
else:
    print 'I am the child'