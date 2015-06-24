import subprocess

p = subprocess.Popen("ps","aux","|","grep", "python", stdout=subprocess.PIPE)

