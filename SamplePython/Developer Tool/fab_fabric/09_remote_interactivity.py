"""
git pull works fine if you’ve already got a checkout of your source code – but what if this is the first deploy? It’d be nice to handle that case too and do the initial git clone:
"""

def deploy():
    code_dir = '/srv/django/myproject'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
        
"""
As with our calls to local above, run also lets us construct clean Python-level logic based on executed shell commands. However, the interesting part here is the git clone call: since we’re using Git’s SSH method of accessing the repository on our Git server, this means our remote run call will need to authenticate itself.

Older versions of Fabric (and similar high level SSH libraries) run remote programs in limbo, unable to be touched from the local end. This is problematic when you have a serious need to enter passwords or otherwise interact with the remote program.

Fabric 1.0 and later breaks down this wall and ensures you can always talk to the other side. Let’s see what happens when we run our updated deploy task on a new server with no Git checkout:
=================
$ fab deploy
No hosts found. Please specify (single) host string for connection: my_server
[my_server] run: test -d /srv/django/myproject

Warning: run() encountered an error (return code 1) while executing 'test -d /srv/django/myproject'

[my_server] run: git clone user@vcshost:/path/to/repo/.git /srv/django/myproject
[my_server] out: Cloning into /srv/django/myproject...
[my_server] out: Password: <enter password>
[my_server] out: remote: Counting objects: 6698, done.
[my_server] out: remote: Compressing objects: 100% (2237/2237), done.
[my_server] out: remote: Total 6698 (delta 4633), reused 6414 (delta 4412)
[my_server] out: Receiving objects: 100% (6698/6698), 1.28 MiB, done.
[my_server] out: Resolving deltas: 100% (4633/4633), done.
[my_server] out:
[my_server] run: git pull
[my_server] out: Already up-to-date.
[my_server] out:
[my_server] run: touch app.wsgi

Done.
=================
Notice the Password: prompt – that was our remote git call on our Web server, asking for the password to the Git server. We were able to type it in and the clone continued normally.
"""