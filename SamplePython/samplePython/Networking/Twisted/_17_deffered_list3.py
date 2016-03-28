from twisted.internet import defer

def got_results(res):
    print 'We got:', res

print 'Two Deferreds.'
d1 = defer.Deferred()
d2 = defer.Deferred()
d = defer.DeferredList([d1, d2])
print 'Adding Callback.'
d.addCallback(got_results)
print 'Firing d1.'
d1.callback('d1 result')
print 'Firing d2.'
d2.callback('d2 result')

"""
    At this point it's pretty clear the result of a DeferredList, 
    at least for the way we've been using it, is a list with the same number of elements as 
    the list of deferreds we passed to the constructor. And the elements of that result 
    list contain the results of the original deferreds, at least if the deferreds succeed. 
    That means the DeferredList itself doesn't fire until all the deferreds in the original list 
    have fired. And a DeferredList created with an empty list fires right away since 
    there aren't any deferreds to wait for.
"""