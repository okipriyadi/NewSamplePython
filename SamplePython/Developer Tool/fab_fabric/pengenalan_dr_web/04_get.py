"""
get (fabric.operations.get)

The get command exists to download (i.e. pull) file(s) from the remote system 
to the computer where the Fabric is being used. It is similar to how scp works and 
comes in handy when you need to download backups, logging data or 
some other server related items.
You can specify the remote path with the remote_path argument.
You can specify the local - download - path with the local_path argument.

Usage examples:
pastikan file 1.png ada di folder home komputer remote
"""
from fabric.api import get
# Download 1.png dari komputer remote ke komputer local
get(remote_path="~/1.png", local_path="~/1.png")

