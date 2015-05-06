"""
Many programs that interact with the user via the terminal need to ask the user for
password values without showing what the user types on the screen. The getpass
module provides a portable way to handle such password prompts securely.
"""
import getpass
import time
import sys
try:
    p = getpass.getpass()
except Exception, err:
    print 'ERROR:', err 
print 'You entered:', p
time.sleep(1)
print "==============use prompt"
try:
    p = getpass.getpass(prompt = "masukan password anda :")
except Exception, err:
    print 'ERROR:', err
else:
    print 'You entered:', p
time.sleep(0.2)    
"""
By default, getpass() uses sys.stdout to print the prompt string. For a pro-
gram that may produce useful output on sys.stdout , it is frequently better to send
the prompt to another stream, such as sys.stderr .
Using sys.stderr for the prompt means standard output can be redirected (to a
pipe or a file) without seeing the password prompt. The value the user enters is still not
echoed back to the screen.
""" 
p = getpass.getpass(stream=sys.stderr)
print 'You entered:', p