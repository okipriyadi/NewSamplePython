"""
Alarms are a special sort of signal, where the program asks the OS to notify it after some
period of time has elapsed. As the standard module documentation for os points out, this
is useful for avoiding blocking indefinitely on an I/O operation or other system call.

In this example, the call to sleep() does not last the full four seconds.
"""

import signal
import time
def receive_alarm(signum, stack):
    print 'Alarm :', time.ctime()

# Call receive_alarm in 2 seconds
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(4)

print 'Before:', time.ctime()
time.sleep(7)
print 'After :', time.ctime()

"""
fungsi receive alarm akan dipanggil ketika waktu tunggunya dalam contoh ini 4 detik dan tidak melewati waktu sleep