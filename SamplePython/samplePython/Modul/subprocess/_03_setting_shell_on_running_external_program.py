"""
Setting the shell argument to a true value causes subprocess to spawn an inter-
mediate shell process, which then runs the command. The default is to run the command
directly.
"""

import subprocess
# Command with shell expansion
subprocess.call('echo $HOME', shell=True)
