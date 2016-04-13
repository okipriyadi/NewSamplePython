"""
Now that we have a project, we can create applications (or “apps” in Django-speak)
within it.To create our blog app, we’ll use manage.py again.
===========================================
./manage.py startapp appsaya
===========================================
# or ".\manage.py startapp blog" on win32

It’s just as simple as starting a project. Now we have a blog directory inside our project
directory.
Like your project, your app is a package too.The models.py and views.py files have
no real code in them; they’re merely placeholders. For our simple blog, in fact, we don’t
need to touch the dummy views.py file at all.

To tell Django this new app is part of your project, you need to edit settings.py
(which we can also refer to as your “settings file”). 

1. Open your settings file in your editor and find the INSTALLED_APPS tuple near the bottom.
2. Add your app in dotted module form to that tuple in a line that looks like this 
   (note the trailing comma): 
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '
    ]
==============================================================+   
   namaproyek.namaaplikasi
   eg: 'mysite.blog',
   lengkapnya menjadi:
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mysite.appsaya'
    ]
    
    atau jika tidak berfungsi coba hilangkan namaproyeknya(langsung nama aplikasinya)
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appsaya'
    ]
==============================================================+

Ketika kita menggunakan 'migrate', django akan melihat SETIAP model.py di SETIAP INSTALLED_APPS 

Django uses INSTALLED_APPS to determine the configuration of various parts of the
system, including the automatic admin application and the testing framework.
"""