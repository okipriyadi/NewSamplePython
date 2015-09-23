"""
ini digunakan jika perintah dijalankan di komputer sendiri bukan untuk komputer remote
local (fabric.operations.local)

As we have mentioned in our introduction, a single Fabric script (fabfile) can 
be used to perform actions both on the local machine and remote system(s). 
For this purpose, Fabric provides the local operative to run commands locally.

Unlike run or sudo, however, interacting with the output of local the same way is 
not possible. Either output can be captured or printed 
-- the switch can be set with capture argument.

Local helpers such as the lcd context manager (which is used for setting the local 
working directory) are honoured with local, the same way run (or sudo) 
honours the cd context manager.

Usage examples:
"""
from fabric.api import local

local("mkdir /tmp/bbb/", capture=False)

local("ls /tmp/")
