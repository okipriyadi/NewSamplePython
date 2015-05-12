"""
To see what signal handlers are registered for a signal, use getsignal() . 
Pass the signal number as argument. The return value is the registered handler or one of the special
values SIG_IGN (if the signal is being ignored), SIG_DFL (if the default behavior is
being used), or None (if the existing signal handler was registered from C, rather than
from Python).

hasilnya akan sangat bervarasi tergantung system operasi apa yang dipakai.
The function for sending signals from within Python is os.kill() . Its use is covered
in the section on the os module, Creating Processes with os.fork().
"""

import signal

def alarm_received(n, stack):
    return

signal.signal(signal.SIGALRM, alarm_received)
signals_to_names = dict((getattr(signal, n), n)
for n in dir(signal)
    if n.startswith('SIG') and '_' not in n)

for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN '
    print '%-10s (%2d):' % (name, s), handler