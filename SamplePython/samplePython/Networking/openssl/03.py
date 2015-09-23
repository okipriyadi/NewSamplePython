from twisted.cred.portal import Portal
from twisted.protocols.ftp import FTPRealm
from twisted.cred.checkers import AllowAnonymousAccess
from cred.ftp_cred import CertPasswordDB

def run():
    portal = Portal(FTPRealm('/home/kyi/delete'), [AllowAnonymousAccess(), CertPasswordDB()])
    reactor.listenTCP(CERT_FTP_PORT, CertFTPFactory(self.fn_uploaded, portal)) #@UndefinedVariable
    reactor.run()  # @UndefinedVariable

if __name__ == '__main__':
    run()