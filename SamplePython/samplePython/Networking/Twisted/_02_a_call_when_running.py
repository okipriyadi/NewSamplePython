"""
reactor tidak akan berfungsi sebelum di run, oleh karena itu tulisan 
"'Hello from the reactor loop!'" 
muncul setelah tulisan 'Starting the reactor.' 

callWhenRunning akan berjlan saat reactor.run() dieksekusi
callWhenRunning harus ditulis sebelum reactor.run karna callWhenRunning 
dieksekusi berbarengan 
dengan saat pertamakali reactor.run dieksekusi  

We use the term callback to describe the reference to the hello function. 
A callback is a function reference that we give to Twisted (or any other framework) 
that Twisted will use to "call us back" at the appropriate time, 
in this case right after the reactor loop starts up


"""
from twisted.internet import reactor

def hello():
    print 'Hello from the reactor loop!'
    print 'Lately I feel like I\'m stuck in a rut.'
 
 
reactor.callWhenRunning(hello) 
print 'Starting the reactor.'
reactor.run()