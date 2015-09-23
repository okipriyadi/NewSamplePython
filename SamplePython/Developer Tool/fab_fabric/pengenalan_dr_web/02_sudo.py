"""
Along with run, the most widely used Fabric command is probably sudo. 
It allows the execution of a given set of commands and arguments with sudo 
(i.e. superuser) privileges on the remote host.

If sudo command is used with an explicitly specified user, 
the execution will happen not as root but another (i.e. UID 1010).

Usage examples:
"""
from fabric.api import sudo

# Create a directory
sudo("mkdir /var/www/test")

# Create a directory as another user
#sudo("mkdir /var/www/web-app-one", user="web-admin")

# Return the output
result = sudo("ls -l /var/www")