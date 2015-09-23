"""
put (fabric.operations.put)
When you need to upload files, put command can be used very similarly to get. 
You can again access the results of command's execution with .failed or .succeeded.

1. local_path - set the local path.
2. remote_path - set the remote path.
3. use_sudo - upload the file to anywhere on the remote machine using a nifty trick: upload to a temporary location then move.
4. mode - set the file mode (flags).
5. mirror_local - set the file flags (i.e. make executable) automatically by reading  the local file's mode.

PASTIKAN file API.odt terdapat di folder home komputer kita
"""
from fabric.api import put, cd

# This will upload api.odt to folder home in the remote machine
put("~/API.odt", "~/API.odt")

# Use the context manager `cd` instead of "remote_path" arg.
# This will upload api.odt to folder /tmp in the remote machine
with cd("/tmp"):
    put("~/API.odt", "API.odt")

# Upload a file and set the exact mode desired
upload = put("~/API.odt", "~/API2.odt", mode=664)

# Verify the upload
upload.succeeded