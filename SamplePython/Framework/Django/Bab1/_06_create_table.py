"""
Now you tell Django to use the connection information you’ve given it to connect to the
database and set up the tables your application needs.The command to do this is simply:
======================================
./manage.py syncdb
======================================
# or ".\manage.py syncdb" on win32

NOTE DI DJANGO TERBARU FASILITAS SYNCDB DIHILANGKAN, sebagai gantinya digunakan
=====================================================================
./manage.py makemigrate #untuk membuat tabel baru
./manage.py migrate #untuk mengupdate tabel
=====================================================================

When you issue the syncdb command, Django looks for a models.py file in each of
your INSTALLED_APPS . For each model it finds, it creates a database table. (There are
exceptions to this later when we get into fancy stuff such as many-to-many relations, but
it’s true for this example. If you are using SQLite, you also notice the django.db database
file is created exactly where you specified.)
"""

