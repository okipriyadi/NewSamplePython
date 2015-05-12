"""
Process Groups / Sessions
If the process created by Popen spawns subprocesses, those children will not receive
any signals sent to the parent. That means when using the shell argument to Popen ,
it will be difficult to cause the command started in the shell to terminate by sending
SIGINT or SIGTERM .
"""

import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/sh
            echo "Shell script in process $$"
            set -x
            python _16_signal_child.py
         '''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name], close_fds=True)
print 'PARENT: Pausing before signaling %s...' % proc.pid
sys.stdout.flush()
time.sleep(1)

print 'PARENT: Signaling child %s' % proc.pid
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)

"""
The pid used to send the signal does not match the pid of the child of the shell
script waiting for the signal, because in this example, there are three separate processes
interacting.
1. The program subprocess_signal_parent_shell.py
2. The shell process running the
script created by the main Python program
3. The program signal_child.py

To send signals to descendants without knowing their process id, use a process
group to associate the children so they can be signaled together. The process group
is created with os.setsid() , setting the “session id” to the process id of the current
process. All child processes inherit their session id from their parent, and since it should
only be set in the shell created by Popen and its descendants, os.setsid() should
not be called in the same process where the Popen is created. Instead, the function is
passed to Popen as the preexec_ fn argument so it is run after the fork() inside the
new process, before it uses exec() to run the shell. To signal the entire process group,
use os.killpg() with the pid value from the Popen instance.

"""