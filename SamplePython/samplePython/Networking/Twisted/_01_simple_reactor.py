"""
 Twisted is an implementation of the Reactor Pattern and thus contains an object that 
 represents the reactor, or event loop, that is the heart of any Twisted program. 
 The first line of our program imports the reactor object so we can use it, 
 and the second line tells the reactor to start running the loop.
 
 reactor adalah looping yang terblok (biasanya dengan select) karna menunggu input dan 
 jika input siap maka looping akan dilanjutkan (event-loop atau juga bisa disebut select loop)

This program just sits there doing nothing. You’ll have to stop it by pressing Control-C, 
otherwise it will just sit there forever. 
"""

from twisted.internet import reactor
reactor.run()
