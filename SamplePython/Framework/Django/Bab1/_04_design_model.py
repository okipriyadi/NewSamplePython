"""
the models.py file.
This is where we’ll define the data structures of our app. 
Let’s create a basic model, and then see all the stuff Django does for us using that information
1. Open up models.py in your favorite text editor 
2. You see this placekeeper text: "from django.db import models # Create your models here."
3. add lines:
=================================================
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
=================================================

That’s a complete model, representing a “BlogPost” object with three fields. (Actually,
strictly speaking it has four fields—Django automatically creates an auto-incrementing,
unique id field for each model by default.)

You can see our newly minted class, BlogPost, is a subclass of
django.db.models.Model .That’s Django’s standard base class for data models, which is
the core of Django’s powerful object-relational mapping system.Also, you notice our fields
are defined like regular class attributes with each one being an instance of a particular field
class.Those field classes are also defined in django.db.models , and there are many more
types—ranging from BooleanField to XMLField—than the three we’re using here.
"""