"""
A double-ended queue, or deque , supports adding and removing elements from either
end. The more commonly used structures, stacks, and queues are degenerate forms of
deques where the inputs and outputs are restricted to a single end.
"""
import collections

d = collections.deque('bcdefgaac')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]
d.remove('c')
print 'remove(c):', d