"""
Once a Counter is populated, its values can be retrieved using the dictionary API.
perhatikan huruf 'e' walaupun tidak terdapat pada counter, tetap tidak enghasilkan error 
Counter does not raise KeyError for unknown items. If a value has not been
seen in the input (as with e in this example), its count is 0 .
"""

import collections
c = collections.Counter('abcdaab')
for letter in 'abcde':
    print '%s : %d' % (letter, c[letter])
