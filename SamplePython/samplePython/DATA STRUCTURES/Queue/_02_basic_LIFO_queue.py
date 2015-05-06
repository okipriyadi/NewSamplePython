import Queue

q = Queue.LifoQueue()
for i in range(5):
    q.put(i)

print q.get()
print q.get()
print q.get()
print q.get()
print q.get()
print q.get()
print q.get()