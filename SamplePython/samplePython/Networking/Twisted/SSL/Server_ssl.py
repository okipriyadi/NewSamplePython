from twisted.internet import reactor 
from twisted.internet.ssl import DefaultOpenSSLContextFactory
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineOnlyReceiver
from OpenSSL.SSL import VERIFY_PEER, VERIFY_FAIL_IF_NO_PEER_CERT

class CtxFactory(DefaultOpenSSLContextFactory):
    def __init__(self):
        DefaultOpenSSLContextFactory.__init__(self, "igg.key", "igg.crt")

    def getContext(self):
        ctx = DefaultOpenSSLContextFactory.getContext(self)
        ctx.set_verify(VERIFY_PEER | VERIFY_FAIL_IF_NO_PEER_CERT, self.verifyCallback)
        ctx.load_verify_locations("rootCA.pem")
        return ctx

    def verifyCallback(self, connection, x509, errnum, errdepth, ok):
        if not ok:
            commonName = x509.get_subject().commonName
            print '"invalid certificate from commonName "'
            return False
        else:
            print "cert ok"
            return True

class SBDAPIFactory(Factory):
    def __init__(self):
        print "========== Starting SBD API handler at port ==========" 

    def buildProtocol(self, addr):
        return SBDAPIProtocol()

    def __del__(self):
        print "========== Stopping SBD API handler =========="


class SBDAPIProtocol(LineOnlyReceiver):
    def __init__(self):
        pass
    
    def connectionMade(self):
        
        peer = self.transport.getPeer()
        print 'connectionmade ========== ' , peer
        cert = self.transport.getPeerCertificate()
        sertifikat = cert.get_subject().commonName
        
        #self.transport.setTcpKeepAlive(1)
        #self.identifyPeer().addCallback(self.verifyEndpoint)

    
    def lineReceived(self, line):
        print 'verifiying ========== ' , peer
        peer = self.transport.getPeer()
        self.processRequest(request, line)

    
reactor.listenSSL (10009, SBDAPIFactory(), CtxFactory())  # @UndefinedVariable
reactor.run()