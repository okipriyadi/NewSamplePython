import os
with open('/home/kyi/delete aja/hapus.py','w+') as f:
    f.write("testing")
try:
    os.remove("hapus.py")
except OSError:
    pass
finally:
    print "yeah"