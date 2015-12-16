"""
Model classes, fields and model instances all map to database concepts:

Thing             Corresponds to...
Model class       Database table
Field instance    Column on a table
Model instance    Row in a database table

When starting to a project with peewee, it's typically best to begin with your data model, 
by defining one or more Model classes:
"""

from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.
        
"""
Note that we named our model Person instead of People. This is a convention you should follow - 
even though the table will contain multiple people, we always name the class using the singular form.
"""

#membuat relasi
"""
Things get interesting when we set up relationships between models using foreign keys.
This is easy to do with peewee:
"""
class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database
   
     
"""
Now that we have our models, let's connect to the database. 
Although it's not necessary to open the connection explicitly, 
it is good practice since it will reveal any errors with your database connection immediately, 
as opposed to some arbitrary time later when the first query is executed. 
It is also good to close the connection when you are done - for instance, 
a web app might open a connection when it receives a request, and close the connection 
when it sends the response.
"""

db.connect()

"""
We'll begin by creating the tables in the database that will store our data. 
This will create the tables with the appropriate columns, indexes, sequences, and foreign key 
constraints:
"""
try:
    db.create_tables([Person, Pet])
except OperationalError:
        print "Artist table already exists!"

