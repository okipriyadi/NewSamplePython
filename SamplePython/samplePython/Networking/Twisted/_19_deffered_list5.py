from twisted.internet import defer

def got_results(res):
    print 'We got:', res

d1 = defer.Deferred()
d2 = defer.Deferred()
d = defer.DeferredList([d1, d2], consumeErrors=True)
d.addCallback(got_results)
print 'Firing d1.'
d1.callback('d1 result')
print 'Firing d2 with errback.'
d2.errback(Exception('d2 failure'))

"""
Now we are firing d1 with a normal result and d2 with an error. Ignore the consumerErrors option for now, we’ll get back to it
Now the tuple corresponding to d2 has a Failure in slot two, and False in slot one. At this point it should be pretty clear how a DeferredList works (but see the Discussion below):

A DeferredList is constructed with a list of deferred objects.
A DeferredList is itself a deferred whose result is a list of the same length as the list of deferreds.
The DeferredList fires after all the deferreds in the original list have fired.
Each element of the result list corresponds to the deferred in the same position as the original list. If that deferred succeeded, the element is (True, result) and if the deferred failed, the element is (False, failure).
A DeferredList never fails, since the result of each individual deferred is collected into the list no matter what (but again, see the Discussion below).

Now let’s talk about that consumeErrors option we passed to the DeferredList. If we run the same code but without passing the option (deferred-list/deferred-list-6.py), we get this output:
=======================================================================================
Firing d1.
Firing d2 with errback.
We got: [(True, 'd1 result'), (False, >twisted.python.failure.Failure >type 'exceptions.Exception'<<)]
Unhandled error in Deferred:
Traceback (most recent call last):
Failure: exceptions.Exception: d2 failure
=======================================================================================

If you recall, the “Unhandled error in Deferred” message is generated when a deferred is garbage collected and the last callback in that deferred failed. The message is telling us we haven’t caught all the potential asynchronous failures in our program. So where is it coming from in our example? It’s clearly not coming from the DeferredList, since that succeeds. So it must be coming from d2.

A DeferredList needs to know when each deferred it is monitoring fires. And the DeferredList does that in the usual way — by adding a callback and errback to each deferred. And by default, the callback (and errback) return the original result (or failure) after putting it in the final list. And since returning the original failure from the errback triggers the next errback, d2 remains in the failed state after it fires.

But if we pass consumeErrors=True to the DeferredList, the errback added by the DeferredList to each deferred will instead return None, thus “consuming” the error and eliminating the warning message. We could also handle the error by adding our own errback to d2

"""