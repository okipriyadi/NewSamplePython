"""
If you want to switch from unencrypted to encrypted traffic mid-connection, 
you'll need to turn on SSL with startTLS on both ends of the connection at the same time 
via some agreed-upon signal like the reception of a particular message. 
You can readily verify the switch to an encrypted channel by examining the packet payloads 
with a tool like Wireshark.
"""

from OpenSSL import SSL
from twisted.internet import reactor, ssl
from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import LineReceiver

class TLSServer(LineReceiver):
    def lineReceived(self, line):
        print "received: " + line

        if line == "STARTTLS":
            print "-- Switching to TLS"
            self.sendLine('READY')
            ctx = ServerTLSContext( privateKeyFileName='igg.key', certificateFileName='igg.crt',)
            self.transport.startTLS(ctx, self.factory)


class ServerTLSContext(ssl.DefaultOpenSSLContextFactory):
    def __init__(self, *args, **kw):
        kw['sslmethod'] = SSL.TLSv1_METHOD
        ssl.DefaultOpenSSLContextFactory.__init__(self, *args, **kw)

if __name__ == '__main__':
    factory = ServerFactory()
    factory.protocol = TLSServer
    reactor.listenTCP(8000, factory)
    reactor.run()