"""
program dibawah ini akan mengubah uid(user ID) dan GID (group id) pada sistem operasi.
cara menjalankan
1. jalankan sebagi root, atau
2. buat dulu satu user dan group baru
   isi TEST_GID dengan GID group baru
   begitu juga dengan UID
"""
import os

TEST_GID= 1000 #isi dengan GID tujuan
TEST_UID= 1000 #isi dengan UID tujuan
def show_user_info():
    print 'User (actual/effective) : %d / %d' % (os.getuid(), os.geteuid())
    print 'Group (actual/effective) : %d / %d' % (os.getgid(), os.getegid())
    print 'Actual Groups:', os.getgroups()
    return

print 'BEFORE CHANGE:'
show_user_info()
print

try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERROR: Could not change effective group.'
else:
    print 'CHANGED GROUP:'
    show_user_info()
    print

try:
    os.seteuid(TEST_UID)
except OSError:
    print 'ERROR: Could not change effective user.'
else:
    print 'CHANGE USER:'
    show_user_info()
    print