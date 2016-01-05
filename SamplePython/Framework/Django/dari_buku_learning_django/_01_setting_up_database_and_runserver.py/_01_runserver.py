"""
As discussed before, Django comes with a lightweight web server for developing and
testing applications. This server is pre-configured to work with Django, and, more
importantly, it restarts whenever you modify the code.
To start the server, run the following command:
============================================================
$ python manage.py runserver
============================================================
Next, open your browser and navigate to this URL: http://localhost:800


As you may have noticed, the web server runs on port 8000 by
default. If you want to change the port, you can specify it on the
command line by using the following command:
===================================================================
$ python manage.py runserver <port number>
===================================================================
Also, the development server is only accessible from the local
machine by default. If you want to access the development
server from another machine on your network, use the following
command-line arguments:
===================================================================
$ python manage.py runserver 0.0.0.0:<port number>
===================================================================
"""