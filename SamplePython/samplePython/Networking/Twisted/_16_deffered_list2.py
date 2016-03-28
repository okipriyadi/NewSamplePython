from twisted.internet import defer

def got_results(res):
    print 'We got:', res

print 'One Deferred.'
d1 = defer.Deferred()
d = defer.DeferredList([d1])
print 'Adding Callback.'
d.addCallback(got_results)
print 'Firing d1.'
d1.callback('d1 result')


"""
More things to notice:

1. This time the DeferredList didn’t fire its callback until we fired the deferred in the list.
2. The result is still a list, but now it has one element.
3. The element is a tuple whose second value is the result of the deferred in the list.
"""