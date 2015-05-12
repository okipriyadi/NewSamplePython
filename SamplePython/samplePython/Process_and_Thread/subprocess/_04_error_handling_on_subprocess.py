import subprocess
try:
    subprocess.check_call(['false'])
except subprocess.CalledProcessError as err:
    print 'ERROR:', err