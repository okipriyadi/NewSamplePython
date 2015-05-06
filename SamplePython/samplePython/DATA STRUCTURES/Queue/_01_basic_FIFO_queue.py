import Queue

q = Queue.Queue()
for i in [5,7,3,2,1]:
    q.put(i)

print q.get()
print q.get()
print q.get()
print q.get()
print q.get()
print q.get()
print q.get()