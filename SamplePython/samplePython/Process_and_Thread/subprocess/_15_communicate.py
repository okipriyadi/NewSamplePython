"""
file ini akan menjalankan file _14_repeater.py yang digunakan sebagai child process 

The next interaction example uses the stdin and stdout file handles owned by
the Popen instance in different ways. In the first example, a sequence of five numbers
is written to stdin of the process, and after each write, the next line of output is read
back. In the second example, the same five numbers are written, but the output is read
all at once using communicate() .
"""
import subprocess
print 'One line at a time:'
proc = subprocess.Popen('python _14_repeater.py', 
                        shell=True, 
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )

for i in range(5):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print output.rstrip()

remainder = proc.communicate()[0]
print remainder
print

print 'All output at once:'
proc = subprocess.Popen('python _14_repeater.py',
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )

for i in range(5):
    proc.stdin.write('%d\n' % i)
    
output = proc.communicate()[0]
print output