"""
To ignore a signal, register SIG_IGN as the handler. This script replaces the default
handler for SIGINT with SIG_IGN and registers a handler for SIGUSR1 . Then it uses
signal.pause() to wait for a signal to be received.

Normally, SIGINT (the signal sent by the shell to a program when the user presses
Ctrl-C ) raises a KeyboardInterrupt . This example ignores SIGINT and raises
SystemExit when it sees SIGUSR1 . Each ^C in the output represents an attempt to
use Ctrl-C to kill the script from the terminal. Using kill -USR1 72598 from an-
other terminal eventually causes the script to exit.
"""

import signal
import os
import time

def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print 'My PID:', os.getpid()
signal.pause()