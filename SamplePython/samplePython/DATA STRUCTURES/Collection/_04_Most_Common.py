"""
This example counts the letters appearing in all words in the system dictionary
to produce a frequency distribution, and then prints the three most common letters.
Leaving out the argument to most_common() produces a list of all the items, in order
of frequency.
"""

import collections
c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

print 'Most common:'
for letter, count in c.most_common(3):
    print '%s: %7d' % (letter, count)