"""
jalankan di command promt dengan memasukan argumen2
"""
import sys
print 'Arguments:', sys.argv

"""
maka hasilnya 
$ python sys_argv.py
Arguments: ['sys_argv.py']
$ python sys_argv.py -v foo blah
Arguments: ['sys_argv.py', '-v', 'foo', 'blah']
$ python -u sys_argv.py
Arguments: ['sys_argv.py']
"""