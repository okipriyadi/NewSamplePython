import os
import os.path
import pprint
def visit(arg, dirname, names):
    print dirname, arg
    for name in names:
        if os.path.isdir(dirname):
            print 'direktory = %s/' % name
        else:
            print 'non direktory =  %s' % name
    print
if not os.path.exists('example'):
    os.mkdir('example')
if not os.path.exists('example/one'):
    os.mkdir('example/one')
with open('example/one/file.txt', 'wt') as f:
    f.write('contents')
with open('example/two.txt', 'wt') as f:
    f.write('contents')
os.path.walk('example', visit, '(User data)')