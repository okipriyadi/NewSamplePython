"""
Ini adalah command untuk komputer yang di remote
mirip dengan penggunaan ssh biasa. 
kita nanti diminta untuk memastikan nama@ipremote
kemudian password komputer remote

run (fabric.operations.run)
Fabric's run procedure is used for executing a shell command on one or more remote hosts.
The output results of run can be captured using a variable.
If command succeeded or failed can be checked using .failed and .succeeded.
"""
from fabric.api import run
# Create a directory 
run("mkdir /tmp/trunk/")

# Uptime    = Melihat jumlah waktu pemakaian komputer oleh seseorang, terhitung proses reboot terakhir.
run("uptime")

# Hostname  = Menampilkan nama komputer
run("hostname")

# Capture the output of "ls" command
result = run("ls -l /tmp")

# Check if command failed
result.failed