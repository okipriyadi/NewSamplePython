from twisted.protocols.ftp import FTPRealm
from twisted.cred.checkers import AllowAnonymousAccess
from twisted.cred.portal import Portal
from twisted.cred.checkers import ICredentialsChecker
from twisted.cred import error, credentials
from zope.interface import implements
from twisted.python import failure
from twisted.internet import defer
from twisted.internet import reactor
from os.path import join, basename
from hashlib import sha1
from ConfigParser import SafeConfigParser
from twisted.protocols import policies
from twisted.protocols.ftp import FTPFactory
from logging import getLogger
from twisted.protocols.ftp import defer, log, FTP, FTPCmdError, BadCmdSequenceError, toSegments, InvalidPath
from twisted.protocols.ftp import FileNotFoundError, FILE_NOT_FOUND, ASCIIConsumerWrapper, DATA_CNX_ALREADY_OPEN_START_XFR
from twisted.protocols.ftp import TXFR_COMPLETE_OK, CNX_CLOSED_TXFR_ABORTED, FILE_STATUS_OK_OPEN_DATA_CNX, WELCOME_MSG
#from apps.models.models import FTPClients
#from libs.mailer import notify_exception


class CertFTP(FTP):
    fn_uploaded = None
    log = getLogger(__name__)
    def connectionMade(self):
    
        peer = self.transport.getPeer()
        print "peer = ", peer
        
        if True:
            self.state = self.UNAUTH
            print "self.state = ", self.state
            self.setTimeout(self.timeOut)
            print "timout =", self.timeOut
            print "welcome_msg =", WELCOME_MSG,   "self factory message =", self.factory.welcomeMessage
            self.reply(WELCOME_MSG, self.factory.welcomeMessage)
            
        else:
            self.log.warning('unknown ftp client %s' % peer.host)
            self.transport.loseConnection()            
        
    def ftp_STOR(self, path):
        if self.dtpInstance is None:
            raise BadCmdSequenceError('PORT or PASV required before STOR')

        try:
            newsegs = toSegments(self.workingDirectory, path)
            print "working directory = ", self.workingDirectory
            print "path======", path
        except InvalidPath:
            return defer.fail(FileNotFoundError(path))

        self.setTimeout(None)

        def enableTimeout(result):
            self.setTimeout(self.factory.timeOut)
            return result

        def cbOpened(file_obj):
            print "test1"
            d = file_obj.receive()
            print "obj receive", d
            print "test2"
            d.addCallback(cbConsumer)
            print "test3"
            d.addCallback(lambda ignored: file_obj.close())
            print "test4"
            d.addCallbacks(cbSent, ebSent)
            print "test5"
            return d

        def ebOpened(err):
            print "testerr1"
            if isinstance(err.value, FTPCmdError):
                print "testerr2"
                return (err.value.errorCode, '/'.join(newsegs))
            print "testerr3"
            log.err(err, "Unexpected error received while opening file:")
            return (FILE_NOT_FOUND, '/'.join(newsegs))

        def cbConsumer(cons):
            if not self.binary:
                cons = ASCIIConsumerWrapper(cons)
                print "cons", cons

            d = self.dtpInstance.registerConsumer(cons)
            print "dtpinstance", d

            if self.dtpInstance.isConnected:
                print "reply : DATA_CNX_ALREADY_OPEN_START_XFR", DATA_CNX_ALREADY_OPEN_START_XFR
                self.reply(DATA_CNX_ALREADY_OPEN_START_XFR)
            else:
                print "DATA_CNX_ALREADY_OPEN_START_XFR" , DATA_CNX_ALREADY_OPEN_START_XFR
                self.reply(FILE_STATUS_OK_OPEN_DATA_CNX)

            return d

        def cbSent(result):
            if callable(self.fn_uploaded):
                peer = self.transport.getPeer()
                print "peer apakah", peer
                self.fn_uploaded(path, peer.host)
                print "suksesss================"
            return (TXFR_COMPLETE_OK,)

        def ebSent(err):
            print "testerr3"
            print ""
            log.err(err, "Unexpected error received during transfer:")
            if err.check(FTPCmdError):
                return err
            return (CNX_CLOSED_TXFR_ABORTED,)

        d = self.shell.openForWriting(newsegs)
        print "d = ", d
        d.addCallbacks(cbOpened, ebOpened)
        print "d after callback = ",  d
        d.addBoth(enableTimeout)
        print "add both ",  d
        return d


class CertFTPFactory(FTPFactory):
    def __init__(self, fn_uploaded, *args, **kwargs):
        assert callable(fn_uploaded)
        FTPFactory.__init__(self, *args, **kwargs)        
        self.fn_uploaded = fn_uploaded
        self.protocol = CertFTP 
        
    def buildProtocol(self, addr):
        p = policies.LimitTotalConnectionsFactory.buildProtocol(self, addr)
        if p is not None:
            p.wrappedProtocol.portal = self.portal
            p.wrappedProtocol.timeOut = self.timeOut
            p.wrappedProtocol.passivePortRange = self.passivePortRange
            p.wrappedProtocol.fn_uploaded = self.fn_uploaded
        return p
        

class CertPasswordDB:    
    implements(ICredentialsChecker)

    def __init__(self):        
        self.credentialInterfaces = (credentials.IUsernamePassword, credentials.IUsernameHashedPassword)        

    def getUser(self, username):
        #entry = FTPUsers.get(FTPUsers.username == username)
        username = 'kyi'
        password = '0608810'
        return (username, password)
        
    def requestAvatarId(self, c):
        def matched(matched, username):
            if matched:
                return username
            else:
                return failure.Failure(error.UnauthorizedLogin())
            
        try:
            username, password = self.getUser('kyi')
        except KeyError:
            return defer.fail(error.UnauthorizedLogin())
        else:
            return defer.maybeDeferred(c.checkPassword, password).addCallback(matched, username)


def check_hash(self, filename):
        with file(filename) as fp:
            hex_hash = sha1(fp.read()).hexdigest()
            computed = '%s.ini' % hex_hash
            return basename(filename) == computed


def import_cert(self, filename, address):
    self.log.info('importing certificate  %s from %s' % (filename, address))                
    with file(filename) as fp:
        parser = SafeConfigParser()
        parser.readfp(fp, filename)
        commonname = parser.get('certificate', 'commonname')
        not_before = parser.get('certificate', 'not_before')
        not_after = parser.get('certificate', 'not_after')
        digest = parser.get('certificate', 'digest')
        
        #update database
        #found = Certificate.update(not_before = not_before, not_after = not_after, digest = digest).where(Certificate.commonname==commonname).execute()
        #if found == 0: 
            #insert database
            #Certificate.insert(commonname=commonname, not_before=not_before, not_after=not_after, digest=digest, active=True).execute()

    

def fn_uploaded(self, result, address):        
        print "result =========", result
        print "address =====", address
        reactor.callLater(0, self.import_cert, join('/home/kyi/delete/', result), address) #@UndefinedVariable
    

def run():
    portal = Portal(FTPRealm('/opt/ffp2/ftp'), [AllowAnonymousAccess(), CertPasswordDB()])
    reactor.listenTCP(2121,CertFTPFactory(fn_uploaded, portal)) #@UndefinedVariable
    reactor.run()  # @UndefinedVariable
    
if __name__ == '__main__':
    run()