"""
Now we’ll write a simple view function that fetches all our blog posts from the database
and displays them using our template. Open up the appsaya/views.py file and type the
following:
======================================================
from django.template import loader, Context
from django.http import HttpResponse
from mysite.blog.models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))
======================================================

Skipping over the import lines for the moment (they just load up the function and
classes we need), here’s the breakdown of the view function, line by line:

Line 5: Every Django view function takes a django.http.HttpRequest object as its
first argument. It can also take other arguments that get passed in via the URLconf,
which is a feature you are using a lot.

Line 6:When we created our appsaya class as a subclass of django.db.models.Model ,
we inherited the full power of Django’s object-relational mapper.This line is a sim-
ple example of using the ORM (Object-Relational Mapper;) to get all the BlogPost objects 
in the database.

Line 7:To create our template object t , we only need to tell Django the name of
the template. Because we’ve stored it in the templates directory of our app, Django
can find it without further instruction.

Line 8: Django templates render data that is provided to them in a context, a dic-
tionary-like object. Our context c has only a single key and value.

Line 9: Every Django view function returns a django.http.HttpResponse object.
In the simplest case, we pass the constructor a string.The template render method
returns a string, conveniently.
"""