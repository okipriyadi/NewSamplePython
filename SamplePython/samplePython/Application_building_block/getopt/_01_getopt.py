"""
parsing command-line arguments
getopt implements the same low-level processing model available to C
programs and shell scripts. It has fewer features than other option-parsing libraries, but
that simplicity and familiarity make it a popular choice

getopt Supported option syntax include short- and long-form options:
-a
-bval
-b val
--noarg
--witharg=val
--witharg val

This example program accepts three options. The -a is a simple flag, while -b and -c
require an argument. The option definition string is "ab:c:" .

getopt.getopt(parameter1, parameter2, parameter3)
- parameter1 is the sequence of arguments to be parsed. This usually comes from sys.argv[1:] 
  (ignoring the program name in sys.arg[0], karna sys.arg[0] hanya berisi full path dari file yg dijalankan
- The second argument is the option definition string for single-character options.
  If one of the options requires an argument, its letter is followed by a colon(titik dua).
- The third argument, if used, should be a sequence of the long-style option names.
  Long-style options can be more than a single character, such as --noarg or
  --witharg . The option names in the sequence should not include the " -- "
  prefix. If any long option requires an argument, its name should have a suffix
  of " = ".
"""
import getopt
from sys import argv
opts, args = getopt.getopt([argv[1], argv[2], argv[3], argv[4]], 'a')
for opt in opts:
    print opt
    
for arg in args:
    print arg
    
    
