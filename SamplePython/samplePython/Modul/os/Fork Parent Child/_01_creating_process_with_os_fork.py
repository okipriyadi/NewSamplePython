"""
The POSIX functions fork() and exec() (available under Mac OS X, Linux, and
other UNIX variants) are exposed via the os module. Entire books have been written
about reliably using these functions, so check the library or a bookstore for more details
than this introduction presents. 

To create a new process as a clone of the current process, use fork() .
"""
import os
print "saya hanya dijalankan satu kali karena saya dieksekusi sebelum forking, "
pid = os.fork()
print "\nini akan diulang dua kali karena dijalankan oleh parent juga childnya"

if pid:
    print 'I am parent process, my Child process has id:', pid
else:
    print 'I am the child'
    
"""
After the fork, two processes are running the same code. For a program to tell
which one it is in, it needs to check the return value of fork() . If the value is 0 , the
current process is the child. 
If it is not 0 , the program is running in the parent process and the return value is 
the process id of the child process.
"""