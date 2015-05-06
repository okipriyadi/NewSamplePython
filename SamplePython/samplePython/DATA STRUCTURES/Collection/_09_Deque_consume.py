import collections
print 'From the right:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.pop(),
    except IndexError:
        break

print
print '\nFrom the left:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.popleft(),
    except IndexError:
        break
print