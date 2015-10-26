from OpenSSL import SSL
from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

class Echo(Protocol):
        
    def dataReceived(self, data):
        ###Ini sebenarnya gak perlu hanya Tambahan jika nanti atributnya diperlukan
        cert = self.transport.getPeerCertificate()
        print cert
        print cert.get_subject().commonName
        print cert.digest('sha1')
        print cert.has_expired()
        
        print "data received: ", data
        data = "dari server dikembalikan ke kamu:" + data
        self.transport.write(data)
        
        
        
def verifyCallback(connection, x509, errnum, errdepth, ok):
    if not ok:
        print 'invalid cert from subject:', x509.get_subject()
        return False
    else:
        print "Certs are fine"
    return True

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo

    myContextFactory = ssl.DefaultOpenSSLContextFactory('igg.key', 'igg.crt')

    ctx = myContextFactory.getContext()

    ctx.set_verify(SSL.VERIFY_PEER | SSL.VERIFY_FAIL_IF_NO_PEER_CERT, verifyCallback)

    # Since we have self-signed certs we have to explicitly
    # tell the server to trust them.
    ctx.load_verify_locations("rootCA.pem")

    reactor.listenSSL(8000, factory, myContextFactory)
    reactor.run()