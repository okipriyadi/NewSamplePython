"""
As used above, fab only really saves a couple lines of if __name__ == "__main__" 
boilerplate. It's mostly designed for use with Fabric's API, 
which contains functions (or operations) for executing shell commands, 
transferring files, and so forth.

Let's build a hypothetical Web application fabfile. 
This example scenario is as follows: 
The Web application is managed via Git on a remote host vcshost. 
On localhost, we have a local clone of said Web application. 
When we push changes back to vcshost, we want to be able to immediately install 
these changes on a remote host my_server in an automated fashion. 
We will do this by automating the local and remote Git commands.

Fabfiles usually work best at the root of a project:

.
|-- __init__.py
|-- app.wsgi
|-- fabfile.py <-- our fabfile!
|-- manage.py
`-- my_app
    |-- __init__.py
    |-- models.py
    |-- templates
    |   `-- index.html
    |-- tests.py
    |-- urls.py
    `-- views.py

Note
We're using a Django application here, but only as an example Fabric is not tied to any external codebase, save for its SSH library.

For starters, perhaps we want to run our tests and commit to our VCS so we're ready for 
a deploy:    
"""

from fabric.api import local

def prepare_deploy():
    local("./manage.py test my_app")
    local("git add -p && git commit")
    local("git push")
    
#The code itself is straightforward: import a Fabric API function, local, and use it to run and interact with 
#local shell commands. The rest of Fabric’s API is similar – it’s all just Python.