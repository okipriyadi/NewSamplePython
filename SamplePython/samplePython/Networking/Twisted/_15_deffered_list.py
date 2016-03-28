from twisted.internet import defer

def got_results(res):
    print 'We got:', res
    return 1
    
def printes(asd):
    print asd
    
print 'Empty List.'
d = defer.DeferredList([])
print 'Adding Callback.'
d.addCallback(got_results)
d.addCallback(printes)
"""
Some things to notice:

1. A DeferredList is created from a Python list. In this case the list is empty, but we’ll soon see that the list elements must all be Deferred objects.
2. A DeferredList is itself a deferred (it inherits from Deferred). That means you can add callbacks and errbacks to it just like you would a regular deferred.
3. In the example above, our callback was fired as soon as we added it, so the DeferredList must have fired right away. We’ll discuss that more in a second.
4. The result of the deferred list was itself a list (empty).
"""