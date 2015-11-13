"""
One of the handiest is Django’s built-in Web
server. It’s a server designed not for deploying public sites, but for quick development.
Advantages of using it include

1. You don’t need to install Apache, Lighttpd, or whatever other Web server software
you’d use in actual production—great if you’re working on a fresh server or a non-
server development machine or just playing around.

2. It automatically detects when you make changes to your Python source files and
reloads those modules.This is a huge time-saver compared to manually restarting
your Web server every time you edit your code, which is what’s required with most
Python Web server setups.

3. It knows how to find and display static media files for the admin application, so you
can work with it right away.

Running the development (or “dev”) server is as simple as issuing a single command.
We’re going to use our project’s manage.py utility, a thin wrapper script that saves us the
work of telling django-admin.py to use our specific project settings file.The command to
run the dev server is
====================================================
./manage.py runserver
====================================================    
"""