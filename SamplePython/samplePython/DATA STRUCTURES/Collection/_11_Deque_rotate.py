"""
Rotating the deque to the right (using a positive rotation) takes items from the
right end and moves them to the left end. Rotating to the left (with a negative value)
takes items from the left end and moves them to the right end. It may help to visualize
the items in the deque as being engraved along the edge of a dial.
"""
import collections

d = collections.deque(xrange(10))
print 'Normal :', d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Right rotation:', d

d = collections.deque(xrange(10))
d.rotate(2)
print 'Left rotation :', d  