#belum berhasil
import fnmatch
class A():
    media = {"sd1S":{"kjshdkajsdj":"ASAs", "ASA":"DASD"}}

b = A()

if fnmatch.fnmatch(b["media"].data, 'sd*'):
    print "match"
else:
    print "doesnt match"