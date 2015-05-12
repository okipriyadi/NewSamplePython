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

def show_setting_sid():
    print 'Calling os.setsid() from %s' % os.getpid()
    sys.stdout.flush()
    os.setsid()

proc = subprocess.Popen(['sh', script_file.name],
                        close_fds=True,
                        preexec_fn=show_setting_sid,
                        )

print 'PARENT: Pausing before signaling %s...' % proc.pid
sys.stdout.flush()
time.sleep(1)

print 'PARENT: Signaling process group %s' % proc.pid
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)

"""
The sequence of events is:
1. The parent program instantiates Popen .
2. The Popen instance forks a new process.
3. The new process runs os.setsid() .
4. The new process runs exec() to start the shell.
5. The shell runs the shell script.
6. The shell script forks again, and that process execs Python.
7. Python runs signal_child.py .
8. The parent program signals the process group using the pid of the shell.
9. The shell and Python processes receive the signal.
10. The shell ignores the signal.
11. The Python process running signal_child.py invokes the signal handler.
"""

