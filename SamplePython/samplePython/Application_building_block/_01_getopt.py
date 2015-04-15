"""
parsing command-line arguments
"""
import getopt
opts, args = getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')
for opt in opts:
    print opt
    
opts, args = getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another',],'', [ 'noarg', 'witharg=', 'witharg2=' ])
for opt in opts:
    print opt