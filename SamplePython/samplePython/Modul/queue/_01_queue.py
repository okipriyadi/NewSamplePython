from Queue import Queue

antrian =  Queue()

a=0
while a <= 200:
    antrian.put((a, a + 1, a + 2))
    a = a+1
    
print antrian.qsize()
(b, c, d) = antrian.get()
print "b,c,d =", b, c, d
print antrian.get()
print antrian.get()
print antrian.get()
print antrian.get()
print type(antrian.get())
print antrian.qsize()

    
