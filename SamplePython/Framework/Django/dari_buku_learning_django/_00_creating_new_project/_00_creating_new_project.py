"""
Untuk membuat proyek baru digunakan perintah
    $ django-admin.py startproject nama_project

ex: 
    $ django-admin.py startproject django_bookmarks
    
akan menghasilkan:

django_bookmarks/
|-- django_bookmarks
    |
    |-- __init__.py
    |
    |-- settings.py
    |
    |-- urls.py
    |
    `-- wsgi.py
`-- manage.py


•     __init__.py : Django projects are Python packages, and this file is required
to tell Python that this folder is to be treated as a package.
A package in Python's terminology is a collection of modules, and they are
used to group similar files together and prevent naming conflicts.

•     manage.py : This is another utility script used to manage our project. You can
think of it as your project's version of the django-admin.py file. Actually,
both django-admin.py and manage.py share the same backend code.

•     settings.py : This is the main configuration file for your Django project. In
it, you can specify a variety of options, including the database settings, site
language(s), what Django features need to be enabled, and so on. Various
sections of this file will be explained as we progress with building our
application during the next chapters, but for this chapter, we will only see
how to enter the database settings.

•     url.py : This is another configuration file. You can think of it as a mapping
between the URLs and Python functions that handle them. This file is one
of Django's powerful features, and we will see how to utilize it in the
next chapter.
"""



