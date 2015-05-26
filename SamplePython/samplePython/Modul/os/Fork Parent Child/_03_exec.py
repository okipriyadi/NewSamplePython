"""
A simple way to handle separate behavior in the child process is to check the
return value of fork() and branch. More complex behavior may call for more code
separation than a simple branch. In other cases, an existing program may need to be
wrapped. For both of these situations, the exec*() series of functions can be used to
run another program.

When a program is run by exec() , the code from that program replaces the code
from the existing process.
"""

import os
child_pid = os.fork()

if child_pid:
    os.waitpid(child_pid, 0)
else:
    os.execlp('pwd', 'pwd', '-P')
    
   