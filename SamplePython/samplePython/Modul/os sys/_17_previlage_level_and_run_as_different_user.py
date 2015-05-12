"""
The first set of functions provided by os is used for determining and changing the
process owner ids. These are most frequently used by authors of daemons or special
system programs that need to change permission level rather than run as root . This
section does not try to explain all the intricate details of UNIX security, process owners,
etc. See the references list at the end of this section for more details.
The following example shows the real and effective user and group information
for a process, and then changes the effective values. This is similar to what a daemon
would need to do when it starts as root during a system boot, to lower the privilege level
and run as a different user.

sebelum menjalankan program coba cek GID(Group ID) dan UID(User ID) di sistem operasinya, untuk linux coba gunakan
cat /etc/passwd. 
ganti GID dan UID dibawah dengan GID & UID yang sesuai

The values do not change because when it is not running as root, a process cannot
change its effective owner value. Any attempt to set the effective user id or group id
to anything other than that of the current user causes an OSError . Running the same
script using sudo so that it starts out with root privileges is a different story.
"""
import os

TEST_GID=1000
TEST_UID=1000

def show_user_info():
    print 'User (actual/effective) : %d / %d' % (os.getuid(), os.geteuid())
    print 'Group (actual/effective) : %d / %d' % (os.getgid(), os.getegid())
    print 'Actual Groups:', os.getgroups()
    return

print 'BEFORE CHANGE:'
show_user_info()


try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERROR: Could not change effective group.rerun as root'
else:
    print 'CHANGED GROUP:'
    show_user_info()
    print

try:
    os.seteuid(TEST_UID)
except OSError:
    print 'ERROR: Could not change effective user. rerun as group'
else:
    print 'CHANGE USER:'
    show_user_info()
    print