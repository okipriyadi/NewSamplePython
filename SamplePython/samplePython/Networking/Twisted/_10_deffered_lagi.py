"""
deffered hanya dipanggil satu kali
hanya bisa dipanggi callback saja atau errback saja
"""
from twisted.internet.defer import Deferred
def out(s): print s
d = Deferred()
d.addCallbacks(out, out)
d.callback('First result')
d.errback(Exception('First error'))
print 'Finished'
