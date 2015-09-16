"""
Specifying connection info at runtime gets old real fast, so Fabric provides a handful 
of ways to do it in your fabfile or on the command line. We won't cover all of them here, 
but we will show you the most common one: setting the global host list, env.hosts.

env is a global dictionary-like object driving many of Fabric's settings, 
and can be written to with attributes as well (in fact, settings, seen above, 
is simply a wrapper for this.) Thus, we can modify it at module level near the 
top of our fabfile like so:
"""
from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = '172.16.191.41'
env.user = 'avionics'
def test():
    result = run("ls ~")
    
"""
When fab loads up our fabfile, our modification of env will execute, storing our settings change. The end result is exactly as above: our deploy task will run against the my_server server.

This is also how you can tell Fabric to run on multiple remote systems at once: because env.hosts is a list, fab iterates over it, calling the given task once for each connection.
"""

