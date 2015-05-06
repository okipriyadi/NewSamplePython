"""
built-in zip berfungsi untuk iterasi yang menghasilkan satu-ke satu. return nya berupa tuple.
contoh zip([1, 2, 3, 4], ['a', 'b', 'c', 'f']) menghasikan 
"""
a = zip([1, 2, 3, 4], ['a', 'b', 'c', 'f'])
for i in a :
    print i
    
print "a = " , a
b = zip([1, 2], ['a', 'b', 'c', 'f'])
print "b =",b
c = zip([1, 2, 3, 4], ['a', 'b', 'c'])
print "c =", c