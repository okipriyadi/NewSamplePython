"""
cd (fabric.context_managers.cd)

cd context manager allows keeping the directory state 
(i.e. where the following block of comments are to be executed). 
It is similar to running the cd command during an SSH session and running various different 
commands.

Usage examples:
"""
from fabric.api import cd, run

# The *cd* context manager makes enwrapped command's
# execution relative to the stated path (i.e. "/tmp/trunk")
with cd("/tmp/trunk"):
    items = run("ls -l")

# It is possible to "chain" context managers
# The run commands gets executed, therefore at "/tmp/trunk"
with cd("/tmp"):
    with cd("/trunk"):
        run("ls")