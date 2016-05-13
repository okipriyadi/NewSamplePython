"""
Only one more piece is needed for our page to work—like anything else on the Web, it
needs a URL. We could create the needed URL pattern directly inside mysite/urls.py , 
but that creates a messy coupling between our project and our app.We can use our blog app some-
where else, so it would be nice if it were responsible for its own URLs.We do this in two
simple steps.

The first step is much like enabling the admin. In mysite/urls.py , there’s a com-
mented example line that is almost what we need. Edit it so it looks like this:
===========================================================+
    url(r'^blog/', include('mysite.blog.urls')),
===========================================================+
NOTE JIKA MUNCUL 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    NameError: name 'include' is not defined
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
maka tambahkan baris berikut:
===========================================================+
    from django.conf.urls import include
===========================================================+

This catches any requests that begin with blog/ and passes them to a new URLconf
you’re about to create.

The second step is to define URLs inside the blog application package itself. Make a
new file, mysite/blog/urls.py , containing these lines:

from django.conf.urls.defaults import *
from mysite.blog.views import archive
===========================================================+
    urlpatterns = patterns('',url(r'^$', archive),)
===========================================================+
NOTE :
don't use it again from django.conf.urls import patterns
You should use a list because patterns() is deprecated since version 1.8, and will be removed in 1.10:
sebagai gantinya pake
===========================================================+
eg:
from django.conf.urls import url    
    urlpatterns =  [
            url(r'^$', archive),
        ]
===========================================================+


JIKA MUNCUL ERROR 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ImportError: No module named defaults
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
maka tambahkan ini jawabannya
django.conf.urls.defaults has been removed in Django 1.6. If the problem was in your own code, you would fix it by changing the import to
=============================================================
from django.conf.urls import patterns, url, include
=============================================================
It looks a lot like our base URLconf.The action happens in line 5. First, note the
part of the request URL, which our root URLconf was matching, is stripped—our
blog application is reusable and shouldn’t care if it’s mounted at blog/ or news/ or
what/i/had/for/lunch/ .The regular expression in line 5 matches a bare URL, such as
/blog/ .

The view function, archive , is provided in the second part of the pattern tuple. (Note
we’re not passing a string that names the function, but an actual first-class function object.
Strings can be used as well, as you see later.)

Let’s see it in action! Is the dev server still running? If not, fire it up with manage.py
runserver , and then go to http://127.0.0.1:8000/blog/ in your browser.You should see a
simple, bare-bones rendering of any blog posts you have entered, complete with title,
timestamp, and post body.
"""