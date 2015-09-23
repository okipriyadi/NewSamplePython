#!/usr/bin/env python

########################################################################################################################
# IMPORTS
########################################################################################################################
from hashlib import sha1
from os import chdir, remove
from os.path import join
from datetime import datetime
from argparse import ArgumentParser
from twisted.internet.protocol import ClientCreator, Protocol
from twisted.internet import reactor
from twisted.protocols.ftp import FTPClient
from StringIO import StringIO
from getpass import getpass
from posix import listdir
from OpenSSL.crypto import load_certificate, FILETYPE_PEM
from ConfigParser import SafeConfigParser
from twisted.internet.defer import Deferred, DeferredList


########################################################################################################################
# FUNCTIONS
########################################################################################################################
class CertUploader(object):
    def __init__(self, server, port, username, path):
        assert isinstance(server, (str, unicode))
        assert isinstance(port, (int, long))
        assert isinstance(username, (str, unicode)), type(username)
        assert isinstance(path, (str, unicode))
        self.server = server
        self.port = port
        self.username = username
        self.path = path

    def extract_certificates(self):
        ret = []
        for filename in listdir(self.path):
            print filename
            if filename.endswith('.crt'):
                filename = join(self.path, filename)
                with open(filename) as fpr:
                    x509 = load_certificate(FILETYPE_PEM, fpr.read())
                    if not x509.has_expired():
                        ret.append(self.extract_certificate(x509))
        return ret

    def extract_certificate(self, x509):
        not_before = x509.get_notBefore()
        not_after = x509.get_notAfter()
        digest = x509.digest('sha1')
        subject = x509.get_subject()
        commonname = subject.commonName
        
        if not_before.endswith('Z'):
            obj_not_before = datetime.strptime(not_before[0:-1], '%Y%m%d%H%M%S')
        else:
            obj_not_before = datetime.strptime(not_before, '%Y%m%d%H%M%S%z')
        
        if not_after.endswith('Z'):
            obj_not_after = datetime.strptime(not_after[0:-1], '%Y%m%d%H%M%S')
        else:
            obj_not_after = datetime.strptime(not_after, '%Y%m%d%H%M%S%z')
        
        output = StringIO()
        cfg_parser = SafeConfigParser()
        cfg_parser.add_section('certificate')
        cfg_parser.set('certificate', 'commonname', commonname)
        cfg_parser.set('certificate', 'not_before', str(obj_not_before))
        cfg_parser.set('certificate', 'not_after', str(obj_not_after))
        cfg_parser.set('certificate', 'digest', digest)
        cfg_parser.write(output)
        str_out = output.getvalue()
        name = sha1(str_out).hexdigest() + '.ini'
        manifest_name = join('/tmp', name)
        with file(manifest_name, 'w') as fpw:
            fpw.write(str_out)
            fpw.flush()
        return name

    def connectionMade(self, client):
        # Get the current working directory
        def finished(results):
            reactor.callLater(1, reactor.stop)  # @UndefinedVariable
        list_manifests = self.extract_certificates()
        DeferredList(map(lambda manifest: self.upload_manifest(client, manifest), list_manifests)).addCallback(finished)

    def connectionFailed(self, reason):
        print "Connection Failed:", reason
        reactor.stop()  # @UndefinedVariable

    def upload_manifest(self, client, manifest):
        assert isinstance(manifest, (str, unicode))
        def uploaded(consumer, manifest, defer):
            chdir('/tmp')
            with open(manifest) as fp:
                consumer.write(fp.read())
                consumer.finish()
            try:
                remove(manifest)
            except OSError:
                pass
            finally:
                defer.callback(None)

        def do_upload_manifest(defer):
            a, b = client.storeFile(manifest)
            a.addCallback(uploaded, manifest, defer)

        defer = Deferred()
        reactor.callLater(0, do_upload_manifest, defer)  # @UndefinedVariable
        return defer

    def run(self):
        password = getpass("Password for %s: " % self.username)
        creator = ClientCreator(reactor, FTPClient, self.username, password.strip(), passive=1)
        creator.connectTCP(self.server, self.port).addCallback(self.connectionMade).addErrback(self.connectionFailed)
        reactor.run()  # @UndefinedVariable


class BufferingProtocol(Protocol):
    """Simple utility class that holds all data written to it in a buffer."""
    def __init__(self):
        self.buffer = StringIO()

    def dataReceived(self, data):
        self.buffer.write(data)

if __name__ == '__main__':
    CertUploader("localhost", "2121", "kyi", "/home/kyi/cert").run()

