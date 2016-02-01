from twisted.application import service
# In particular, we will be using the Application function to create a new application 
# service . An application service simply acts as a central object on which to store certain kinds of 
# deployment configuration.
application = service.Application("SMTP Client Tutorial")
"""
creates a new application service and binds it to the local name application .
twistd requires this local name in each .tac file it runs. It uses various pieces 
of configuration on the object to determine its behavior. For example, 
"SMTP Client Tutorial" will be used as the name of the .tap file into which to 
serialize application state, should it be necessary to do so.

twistd -ny _01_mailer.py

we are rewarded with the following output:

exarkun@boson:~/mail/tutorial/smtpclient$ twistd -ny smtpclient-1.tac
18:31 EST [-] Log opened.
18:31 EST [-] twistd 2.0.0 (/usr/bin/python2.4 2.4.1) starting up
18:31 EST [-] reactor class: twisted.internet.selectreactor.SelectReactor
18:31 EST [-] Loading smtpclient-1.tac...
18:31 EST [-] Loaded.

As we expected, not much is going on. We can shutdown this server by issuing ^C :
"""
