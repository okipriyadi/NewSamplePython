"""
To prevent error messages from commands run through check_output() from
being written to the console, set the stderr parameter to the constant STDOUT .
"""

import subprocess
try:
    output = subprocess.check_output('echo to stdout; echo to stderr 1>&2; exit 1',
                                    shell=True,
                                    stderr=subprocess.STDOUT,
                                    )
except subprocess.CalledProcessError as err:
    print 'ERROR:', err
else:
    print 'Have %d bytes in output' % len(output)
