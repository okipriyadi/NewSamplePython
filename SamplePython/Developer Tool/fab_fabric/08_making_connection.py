"""
Let’s start wrapping up our fabfile by putting in the keystone: 
a deploy task that is destined to run on one or more remote server(s), 
and ensures the code is up to date:
"""
from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def deploy():
    code_dir = '/srv/django/myproject'
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
        
"""
Here again, we introduce a handful of new concepts:

1. Fabric is just Python, so we can make liberal use of regular Python code constructs 
such as variables and string interpolation;
2. cd, an easy way of prefixing commands with a cd /to/some/directory call. 
This is similar to lcd which does the same locally.
3. run, which is similar to local but runs remotely instead of locally.
We also need to make sure we import the new functions at the top of our file
"""


