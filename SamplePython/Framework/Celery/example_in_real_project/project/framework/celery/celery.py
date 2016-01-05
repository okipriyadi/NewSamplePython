from __future__ import absolute_import

from celery import Celery

# instantiate Celery object
celery = Celery(include=[
                         'framework.email.email_tasks'
                        ])

# import celery config file
celery.config_from_object('celeryconfig')

if __name__ == '__main__':
    celery.start()
    
"""
The two commented portions here can be a bit confusing.

    celery = Celery(include=['framework.email.email_tasks'])

Here we are instantiating a Celery object and handing it a list containing the relative 
(to where you start your Celery daemon!) path to all modules containing Celery tasks.

    celery.config_from_object('celeryconfig')

Next, we are telling that newly instantiated Celery object to import its configuration settings from celeryconfig.



Headache Number One: Celery and relative imports

I'm sad to admit that it look me 15 minutes figure out why I didn't need celeryconfig.py in the same 
directory as my celery.py. So, read this and learn from my stupid mistake.

Again, I want to emphasize everything is relative to where the Celery daemon is launched.

Our Celery daemon will be launched from /
Because the config file is located at /celeryconfig.py
The daemon looks for the config file in the root: celeryconfig
Additionally the module containing tasks is located several directories deep: /framework/email/email_tasks.py
So the daemon thinks the email_tasks.py is located several directories deep framework.email.email_tasks



"""