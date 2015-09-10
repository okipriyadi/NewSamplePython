
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['my_server']

def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

def commit():
    local("git add -p && git commit")

def push():
    local("git push")

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
        
"""
This fabfile makes use of a large portion of Fabric’s feature set:

1. defining fabfile tasks and running them with fab;
2. calling local shell commands with local;
3. modifying env vars with settings;
4. handling command failures, prompting the user, and manually aborting;
5. and defining host lists and run-ning remote commands.
However, there’s still a lot more we haven’t covered here! Please make sure you follow the various “see also” links, and check out the documentation table of contents on the main index page.
"""