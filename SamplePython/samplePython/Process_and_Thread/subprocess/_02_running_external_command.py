"""
To run an external command without interacting with it in the same way as
os.system() , use the call() function.
"""
import subprocess
# Simple command
subprocess.call(['ls', '-1'])
