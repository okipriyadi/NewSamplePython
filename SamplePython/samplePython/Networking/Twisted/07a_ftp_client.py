from twisted.internet.protocol import ClientCreator
from twisted.protocols.ftp import FTPClient
from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList

def upload_manifest(client, manifest):
        assert isinstance(manifest, (str, unicode))
        def uploaded(consumer, manifest, defer):
            print "consumer", consumer
            print "manifest", manifest
            with open(manifest) as fp:
                print "fp.read =", fp.read()
                consumer.write(fp.read())
                
                consumer.finish()
            defer.callback(None)
            
        def do_upload_manifest(defer):
            a, b = client.storeFile(manifest)
            print "a", a
            print "b", b
            a.addCallback(uploaded, manifest, defer)
        
        print "client", client
        print "manifest", manifest
        defer = Deferred()
        reactor.callLater(0, do_upload_manifest, defer)  # @UndefinedVariable
        return defer

def connectionMade(client):
    # Get the current working directory
    
    def finished(results):
        reactor.callLater(1, reactor.stop)  # @UndefinedVariable
    print "client",client
    list_manifests = '07b_file.ini'
    upload_manifest(client, list_manifests)
    

def connectionFailed(reason):
    print "Connection Failed:", reason
    reactor.stop()  # @UndefinedVariable

def run():
    password = '0608810'
    creator = ClientCreator(reactor, FTPClient, 'kyi', password.strip(), passive=1)
    creator.connectTCP('127.0.0.1', 2121).addCallback(connectionMade).addErrback(connectionFailed)
    reactor.run()  # @UndefinedVariable

    
if __name__ == '__main__':
    run()