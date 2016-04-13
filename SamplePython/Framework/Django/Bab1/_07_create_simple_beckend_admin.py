"""
Because halaman admin ini adalah optional part of Django, you need to specify in your 
settings.py file. 
1. Open settings.py 
2. add the following line to the INSTALLED_APPS tuple, just underneath
    'django.contrib.auth' ,
    'django.contrib.admin',
3. Every time you add a new application to your project, you should run the syncdb
    command to make sure the tables it needs have been created in your database. Here we
    can see adding the admin app to INSTALLED_APPS and running syncdb triggers the cre-
    ation of one more table in our database:
    $ ./manage.py syncdb
    
Now that the app is set up, all we need to do is give it a URL so we can get to it.You
should have noticed these two lines in your automatically generated urls.py .
=====================================================+
# Uncomment this for admin:
# (r'^admin/', include('django.contrib.admin.urls')),
=====================================================+
Remove the # character from the second line (and you can remove the first, comment-
only line at the same time) and save the file.You’ve told Django to load up the default
admin site, which is a special object used by the contrib admin application.

Finally, your applications need to tell Django which models should show up for editing
in the admin screens.To do so, you simply need to define the default admin site men-
tioned previously and register your BlogPost model with it. OPEN the
sitesaya/blog/models.py file, MAKE SURE the admin application is IMPORTED, and then ADD
a line REGISTERING your model at the bottom.
=====================================================+
from django.db import models
from django.contrib import admin     # <----------------pastikan ini ada

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

admin.site.register(BlogPost)        # <----------------tambahkan baris ini untuk meregistrasikanya
=====================================================+
Trying Out the admin
Now that we’ve set up our Django site with the admin app and registered our model with
it, we can take it for a spin. Issue the manage.py runserver command again. Now, go to
http://127.0.0.1:8000/admin/ in your Web browser. (Don’t worry if your dev server
address is different; just add an admin/ onto it, whatever it is.) You should see a login
screen.

Type the “superuser” name and password you created earlier when create a database table . 
Once you’ve logged in, you see the admin home page

JIKA BELUM PUNYA SUPER USER, KITA BISA MEMBUATNYA DENGAN CARA(note : command is only available if 'django.contrib.auth' is in your INSTALLED_APPS)
=================================================================
    ./manage.py createsuperuser
=================================================================

Tip
The three most common causes for “My app doesn’t show up in the admin,” problems are
1) forgetting to register your model class with admin.site.register , 
2) errors in the app’s models.py , and 
3) forgetting to add the app to the INSTALLED_APPS tuple in your settings.py file.
"""