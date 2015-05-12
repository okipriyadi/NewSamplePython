"""
Cari tau apa beda signal.SIGINT, signalSIGUSR1, signalSIGUSR2 

"""

import os
import signal

os.kill(5610, signal.SIGINT) #Argument1 : PID process yang ingin di kill