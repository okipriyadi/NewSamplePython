from posix import listdir
from os.path import join
from OpenSSL.crypto import load_certificate, FILETYPE_PEM


for filename in listdir("cert"):
    print filename
    if filename.endswith('.crt'):
        filename = join("cert", filename)
        with open(filename) as fpr:
            x509 = load_certificate(FILETYPE_PEM, fpr.read())
            print "x509 = " , x509
            print "has expired = ", x509.has_expired()
            print "not before = ", x509.get_notBefore()
            print "not after = ", x509.get_notAfter()
            print "digest sha1 = ", x509.digest('sha1')
            print "digest sha256 = ", x509.digest('sha256')
            print "digest md5 = ", x509.digest('md5')
            print "get_subject = ", x509.get_subject()
            CN = x509.get_subject()
            print "CommonName = ", CN.commonName
            
            
            from datetime import datetime
            if x509.get_notBefore().endswith('Z'):
                print "masuk sini"
                obj_not_before = datetime.strptime(x509.get_notBefore()[0:-1], '%Y%m%d%H%M%S')
                print obj_not_before
            else:
                print "masuk sono"
                obj_not_before = datetime.strptime(x509.get_notBefore(), '%Y%m%d%H%M%S%z')
            
            if x509.get_notAfter().endswith('Z'):
                print "masuk sini"
                obj_not_after = datetime.strptime(x509.get_notAfter()[0:-1], '%Y%m%d%H%M%S')
                print obj_not_before
            else:
                print "masuk sono"
                obj_not_after = datetime.strptime(x509.get_notAfter(), '%Y%m%d%H%M%S%z')
            
            from StringIO import StringIO
            from ConfigParser import SafeConfigParser
            output = StringIO()
            
            cfg_parser = SafeConfigParser()
            cfg_parser.add_section('certificate')
            cfg_parser.set('certificate', 'commonname', CN.commonName)
            cfg_parser.set('certificate', 'not_before', str(obj_not_before))
            cfg_parser.set('certificate', 'not_after', str(obj_not_after))
            cfg_parser.set('certificate', 'digest', x509.digest('sha1'))
            cfg_parser.write(output)
            str_out = output.getvalue()
            print "str_out = ", str_out
            from hashlib import sha1
            name = sha1(str_out).hexdigest() + '.ini'
            print "name = ", name
            manifest_name = join('/tmp', name)
            with file(manifest_name, 'w') as fpw:
                fpw.write(str_out)
                fpw.flush()
            print "=========================================\n"