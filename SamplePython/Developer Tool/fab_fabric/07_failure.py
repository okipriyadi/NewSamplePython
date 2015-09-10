"""
Our base case works fine now, but what happens if our tests fail? Chances are we want to put on the brakes and fix them before deploying.

Fabric checks the return value of programs called via operations and will abort if they didn’t exit cleanly. Let’s see what happens if one of our tests encounters an error:

We didn’t have to do anything ourselves: Fabric detected the failure and aborted, never running the commit task.
But what if we wanted to be flexible and give the user a choice? 
A setting (or environment variable, usually shortened to env var) 
called warn_only lets you turn aborts into warnings, allowing flexible error handling 
to occur.

Let’s flip this setting on for our test function, and then inspect the result of the 
local call ourselves:
"""

from __future__ import with_statement
from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")

#[...]

"""
In adding this new feature we’ve introduced a number of new things:

The __future__ import required to use with: in Python 2.5;
Fabric’s contrib.console submodule, containing the confirm function, 
used for simple yes/no prompts;

The settings context manager, used to apply settings to a specific block of code;
Command-running operations like local can return objects containing info about their result
(such as .failed, or .return_code);


And the abort function, used to manually abort execution.
However, despite the additional complexity, it’s still pretty easy to follow, 
and is now much more flexible.
"""
