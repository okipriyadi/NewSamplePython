from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    length = models.IntegerField()


"""
    As you can see, Django uses Python classes to represent objects, which generally map
to SQL tables with attributes mapping to columns.These attributes are themselves
objects, specifically subclasses of a Field parent class; as stated previously, some of them
are obvious analogues to SQL column types, although others provide some level of
abstraction. Let’s examine some specific Field subclasses.

1.CharField and TextField : Possibly the most common fields you encounter, these two do much the same thing—they 
    hold text. CharField s have a set, finite length, although TextField s are essentially infinite; 
    which one you use depends on your needs, including the fulltext search capabilities of your database 
    or your need for efficient storage.
2 EmailField , URLField , and IPAddressField :These three fields, among others, are essentially CharFields 
   which provide extra validation. Such fields are stored in the database, like a CharField but have 
   validation code defined to ensure their values conform to e-mail addresses, URLs, and IP addresses, 
   respectively. It’s simple to add your own validation to model fields and thus to create your own 
   “field types” on the same level as Django’s built-in ones. (See Chapters 6,“Templates and Form
   Processing,” and 7,“Photo Gallery,” for more on validation.)
3. Boolean Field and NullBooleanField : BooleanField works in most situations where you want to store 
   True or False values, but sometimes you want the capability to store the fact you don’t know yet 
   if the value is one or the other—in which case the field would be considered empty, or null, 
   and thus NullBooleanField was born.This distinction highlights the fact that modeling your data 
   often requires some thought, and decisions sometimes need to be made on a semantic level as well
   as a technical one—not just how the data is stored, but what it means.
4. FileField : FileField is one of the most complex fields, in no small part because almost all 
   the work involved in its use isn’t in the database at all, but in the request part of the framework. 
   FileField stores only a file path in the database, similar to its lesser cousin FilePathField , 
   but goes the extra mile and provides the capability to upload a file from the user’s browser and 
   store it somewhere on the server. It also provides methods on its model object for accessing a 
   Web-based URL for the uploaded file.   

"""