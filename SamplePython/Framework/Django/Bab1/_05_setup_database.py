"""
settings.py

If you don’t have a database server installed and running, we recommend SQLite as the
fastest and easiest way to get going. It’s fast, widely available, and stores its database as 
a single file in the filesystem. Access controls are simply file permissions. 

If you do have a database server—PostgreSQL, MySQL, Oracle, MSSQL—and want to
use it rather than SQLite, then use your database’s administration tools to create a new
database for your Django project. We name this database “djangodb” in our examples, but
you can name it whatever you like.

Either way, with your (empty) database in place, all that remains is to tell Django how
to use it.This is where your project’s settings.py file comes in.

Many people use Django with a relational database server such as PostgreSQL or MySQL.
There are six potentially relevant settings here (though you may need only two):
DATABASE_ENGINE , DATABASE_NAME , DATABASE_HOST , DATABASE_PORT , DATABASE_USER ,
and DATABASE_PASSWORD .Their names make their respective purposes pretty obvious. Just
plug in the correct values corresponding to the database server you are using with Django.
For example, settings for MySQL look something like this:
===============================================
DATABASE_ENGINE = "mysql"
DATABASE_NAME = "djangodb"
DATABASE_HOST = "localhost"
DATABASE_USER = "paul"
DATABASE_PASSWORD = "pony" # secret!
===============================================
Note
We haven’t specified DATABASE_PORT because that’s only needed if your database server is
running on a nonstandard port. For example, MySQL’s server uses port 3306 by default.
Unless you’ve changed the setup, you don’t have to specify DATABASE_PORT at all.

Using SQLite
SQLite is a popular choice for testing and even for deployment in scenarios where there
isn’t a great deal of simultaneous writing going on. No host, port, user, or password infor-
mation is needed because SQLite uses the local filesystem for storage and the native
filesystem permissions for access control. So only two settings are needed to tell Django to
use your SQLite database.
===============================================
DATABASE_ENGINE = "sqlite3"
DATABASE_NAME = "/var/db/django.db"
===============================================
Note
When using SQLite with a real Web server such as Apache, you need to make sure the
account owning the Web server process has write access both for the database file itself
and the directory containing that database file. When working with the dev server like we are
here, permissions are typically not an issue because the user (you) running the dev server
also owns the project files and directories.

SQLite is also one of the most popular choices on Win32 platforms because it comes
free with the Python distribution. Given we have already created a C:\py\django direc-
tory with our project (and application), let’s create a db directory as well.
===============================================
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = r'C:\py\django\db\django.db'
===============================================
"""