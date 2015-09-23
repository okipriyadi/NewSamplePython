"""
reboot (fabric.operations.reboot)

The reboot command is also self explanatory: it is used to reboot the remote system. 
By default, it waits two minutes (i.e. 120 seconds -> wait=120) before doing its job.

Usage examples:
"""
from fabric.api import reboot
# Reboot the remote system
reboot()

# Reboot after 30 seconds
reboot(wait=30)