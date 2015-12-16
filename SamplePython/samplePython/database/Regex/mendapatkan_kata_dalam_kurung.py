import re

a = 'English "Hello", Spanish "Hola"'
b = re.search(".+", a)
print b.group()

"""
We may expect that it matches "Hello" and "Hola" but it will actually match "Hello",
Spanish "Hola" .
This behavior is called greedy and is one of the two possible behaviors of the
quantifiers in Python: greedy and non-greedy (also known as reluctant).
1. The greedy behavior of the quantifiers is applied by default in the quantifiers. A greedy quantifier will try to match as much as possible to have the bigge
2. The non-greedy behavior can be requested by adding an extra question mark to the quantifier; for example, ?? , *? or +? . A quantifier marked as reluctant will behave like the exact opposite of the greedy ones. They will try to have the smallest match possible.
"""
a = 'English "Hello", Spanish "Hola"'
b = re.search(".+?", a)
print b.group()