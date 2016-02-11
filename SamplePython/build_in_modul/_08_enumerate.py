#enumerate memberian angka otomatis pada list
a = ['a', 'b', 'c', 'd']
b = enumerate(a)
print "b = ", b
for c in b:
    print c

print "\n========= mulai dari angka 1 bukan 0"    
d = enumerate(a, start = 1)
for e in d:
    print e