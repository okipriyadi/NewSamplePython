"""
Let's begin by populating the database with some people. 
We will use the save() and create() methods to add and update people's records.
"""
from _01_Membuat_definisi_model import Person, Pet, db
from datetime import date
from peewee import *

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
print uncle_bob
uncle_bob.save() # bob is now stored in the database

#When you call save(), the number of rows modified is returned.

"""
You can also add a person by calling the create() method, which returns a model instance:
"""

grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

"""
To update a row, modify the model instance and call save() 
to persist the changes. Here we will change Grandma's name and then save the changes 
in the database:
"""
grandma.name = 'Grandma L.'
grandma.save()  # Update grandma's name in the database.


"""
Add pets
"""
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

"""
Remove pets
"""
herb_mittens.delete_instance() 
"""
The return value of delete_instance() is the number of rows removed from the database.
"""

"""
change owner
Uncle Bob decides that too many animals have been dying at Herb's house, so he adopts Fido:
"""
herb_fido.owner = uncle_bob
herb_fido.save()
bob_fido = herb_fido # rename our variable for clarity


"""
Mengambil data
To get a single record from the database, use SelectQuery.get():
"""
grandma = Person.select().where(Person.name == 'Grandma L.').get()

"""
We can also use the equivalent shorthand Model.get():
"""
grandma = Person.get(Person.name == 'Grandma L.')

print grandma;

"""
Lists of records
Let's list all the people in the database:
"""
for person in Person.select():
    print person.name, person.is_relative
    
query = Pet.select().where(Pet.animal_type == 'cat')
for pet in query:
    print pet.name, pet.owner.name

"""
There is a big problem with the previous query: because we are accessing pet.owner.name 
and we did not select this value in our original query, 
peewee will have to perform an additional query to retrieve the pet's owner. 
This behavior is referred to as N+1 and it should generally be avoided.

We can avoid the extra queries by selecting both Pet and Person, and adding a join.
"""
query = (Pet
         .select(Pet, Person)
         .join(Person)
         .where(Pet.animal_type == 'cat'))

for pet in query:
    print pet.name, pet.owner.name
    
#Let's get all the pets owned by Bob:
for pet in Pet.select().join(Person).where(Person.name == 'Bob'):
    print pet.name
    
#We can do another cool thing here to get bob's pets. Since we already have an object to represent Bob, we can do this instead:
for pet in Pet.select().where(Pet.owner == uncle_bob):
    print pet.name
    
#Let's make sure these are sorted alphabetically by adding an order_by() clause:
for pet in Pet.select().where(Pet.owner == uncle_bob).order_by(Pet.name):
    print pet.name
    
#Let's list all the people now, youngest to oldest:
for person in Person.select().order_by(Person.birthday.desc()):
    print person.name, person.birthday
    
#Now let's list all the people and some info about their pets:
for person in Person.select():
    print person.name, person.pets.count(), 'pets'
    for pet in person.pets:
        print '    ', pet.name, pet.animal_type
        
#Once again we've run into a classic example of N+1 query behavior. We can avoid this by performing a JOIN and aggregating the records:
subquery = Pet.select(fn.COUNT(Pet.id)).where(Pet.owner == Person.id)
query = (Person
         .select(Person, Pet, subquery.alias('pet_count'))
         .join(Pet, JOIN.LEFT_OUTER)
         .order_by(Person.name))

for person in query.aggregate_rows():  # Note the `aggregate_rows()` call.
    print person.name, person.pet_count, 'pets'
    for pet in person.pets:
        print '    ', pet.name, pet.animal_type
        
"""
Even though we created the subquery separately, only one query is actually executed.

Finally, let's do a complicated one. Let's get all the people whose birthday was either:

before 1940 (grandma)
after 1959 (bob)
"""
d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person
         .select()
         .where((Person.birthday < d1940) | (Person.birthday > d1960)))

for person in query:
    print person.name, person.birthday
    
query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))

for person in query:
    print person.name, person.birthday
    
#Now let's do the opposite. People whose birthday is between 1940 and 1960:

query = (Person
         .select()
         .where((Person.birthday > d1940) & (Person.birthday < d1960)))

for person in query:
    print person.name, person.birthday
    
#One last query. This will use a SQL function to find all people whose names start with either an upper or lower-case G:
expression = (fn.Lower(fn.Substr(Person.name, 1, 1)) == 'g')
for person in Person.select().where(expression):
    print person.name
    
    
#We're done with our database, let's close the connection:

db.close()