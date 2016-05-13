"""
Familiarization with the Django models
Models are the standard Python classes with some added features. They are subclasses
of django.db.models.Model . In the background, an Object-Relational Mapper
(ORM) gets bound with these classes and their objects. This makes them communicate
with the underlying database. ORM is one of the important features of Django, without
which we will end up writing our own queries (SQL, if its MySQL) to access the
database content. Each attribute of a model is represented by a database field. Without
its fields, a model will be just like an empty container, with no meaning whatsoever.
The following are Django's model attributes explained with their intended
use. A complete list of fields can be found on the stranded documentation at
https://docs.djangoproject.com/en/dev/ref/models/fields/ .
Following is a partial table of these types:

Field type         Description
IntegerField       an integer
TextField          A large text field
DateTimeField      A date-and-time field
EmailField         An e-mail field with 75 characters maximum
URLField A         URL field with 200 characters maximum
FileField          A file-upload field

Each model field takes a set of field-specific arguments. For example, if we want
a field to be a CharField field, we must pass its max_length parameter as its
argument, which is mapped to the field size in varchar to the database.
The following are the arguments that can be applied to all the field types (they
are optional):

•     null : By default, it is set to false . When set to true , the associated field is 
      allowed to have a value of null stored in the database.
•     blank : By default, it is set to false . When set to true , the associated field is 
      allowed to have a value of blank stored in the database. The difference between the null and blank 
      parameters is that the null parameter is mainly database-related, whereas the blank parameter 
      is used for validating the field. In other words, if the attribute is set to false, the empty 
      value (blank) for the attribute will not get saved.
•     choices : This can be a list or a tuple and must be iterable. If this is in the form of a tuple, 
      the first element is the value that will get stored to the database and the second value is 
      used for display in widget-like forms or ModelChoiceField . For example: 
      USER_ROLE = (('U', 'USER'), ('S', 'STAFF'), ('A', 'ADMIN'))
      user_role = models.CharField(max_length=1, choices=USER_ROLE)
•     default : Values that are assigned to the attribute every time an object of the class is instantiated.
•     help_text : Help text displayed in the form of a widget.
•     primary_key : If set to True , this field is made primary key for the model. If there is no primary 
      key in the model, Django will create an integer field and mark that as the primary key.
      
Relationships in models
    There are three major types of relationships: many-to-one, many-to-many, and one-to-one.

Many-to-one relationships
-------------------------
    In Django, the django.db.models.ForeignKey parameter is used to define a model as a foreign key 
    to another model's attribute, which results in a many-to-many relationship.
    
It is used as any other attribute of a model class, after including the class in which it
is present. For example, if students study in a particular school, the relationship is
that the school has many students but a student goes to only one school, making this
a many-to-one relationship. Let's take a look at the following code snippet:
========================================================================
from django.db import models
class School(models.Model):
    # ...
    ass

class Student(models.Model):
    school = models.ForeignKey(School)
    # ...
========================================================================

One-to-one relationships
------------------------
One-to-one relationships are very similar to many-to-one relationships. The only
difference is that reverse mapping results in a single object in the case of one-to-one
as opposed to many-to-one relationships.
For example:
class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry)
    details = models.TextField()

In the preceding example, the EntryDetail() class has an attribute called entry ,
which is mapped one-to-one with the Entry model. This means that every Entry
object has been mapped to the EntryDetail model.


Many-to-many relationships
As the name itself suggests, model attributes with many-to-many relationships
provide access to both the models it's been pointed to (like backward one-to-many
relationships). Attribute naming is the only significant difference between the two relationships.
This will be clearer if we go through the following example:
class Product(models.Model):
    name = models.CharField(_(u"Name"), max_length=50)

class Category(models.Model):
name = models.CharField(_(u"Name"), max_length=50)
products = models.ManyToManyField("Product", blank=True, null=True)

With the idea of attribute and primary relationships, we can now straightaway create
our projects model, which we will soon be doing in the coming sections.
If we are going to design the model for an application, we should break up the
applications if it has too many models. If we have more than roughly 15 models in
our application, we should think about the ways in which to break our application
into smaller applications. This is because, with the existing 15-model application,
we are probably doing way too many things. This doesn't go with the Django
philosophy of an app should do one thing and do it right.
"""

