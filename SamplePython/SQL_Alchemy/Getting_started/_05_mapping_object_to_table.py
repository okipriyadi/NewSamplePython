#In order to use the ORM, we need to import the appropriate names:
from sqlalchemy.orm import *

from sqlalchemy import *
from datetime import datetime

metadata = MetaData('sqlite:///tutorial.sqlite')
user_table = Table('tf_user', metadata,
                   Column('id', Integer, primary_key = True), 
                   Column('user_name', String(16), unique=True, nullable=False),
                   Column('password', String(40), nullable=False),
                   Column('display_name', String(40)),
                   Column('created', DateTime, default= datetime.now)
                   )

group_table = Table('tf_group', metadata, 
                    Column('id', Integer, primary_key=True),
                    Column('group_name', String(16),unique=True, nullable=False)
                    )

permission_table = Table('tf_permission', metadata, 
                         Column('id', Integer, primary_key=True),
                         Column('permission_name', String(16),unique=True, nullable=False)
                         )

user_group_table = Table('tf_user_group', metadata,
                         Column('user_id', None, ForeignKey('tf_user.id'), primary_key=True),
                         Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True)
                         )

group_permission_table = Table('tf_group_permission', metadata, 
                            Column('permission_id', None, ForeignKey('tf_permission.id'), primary_key=True),
                            Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True)
                           )

"""
The simplest case of mapping is to just declare empty classes for our application objects
and declare an empty mapper:
"""

class User(object): pass
class Group(object): pass
class Permission(object): pass
mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)

"""
Now that we have declared the mapping between our classes and tables, we can start
doing queries. First off, though, we need to understand the unit of work (UOW) pat-
tern. In UOW as implemented by SQLAlchemy, there is an object known as a
Session that tracks changes to mapped objects and can flush ( ) them out en masse to
the database in a single "unit of work." This can lead to substantial performance im-
provement when compared to executing multiple separate updates. In SQLAlchemy,

the Session class is created using the sessionmaker ( ) function, and the Session object
is created by instantiating the class returned from sessionmaker ( ). The intent is that
sessionmaker ( ) should be called once (at the module level), with its return value used
to create individual sessions.
"""
#create session class
Session = sessionmaker()
#create session object
session = Session()
#Once we have the session object, we use it to obtain access to a Query object for our class:
query = session.query(User)
"""
The simplest way to use the Query object is as an iterator for all the objects in the
database. Since we have already inserted a row in the user_table , we can retrieve that
row as a User object:
"""
list(query)
for user in query:
    print user.user_name
    
"""
we can also retrieve object from the database by using its primary key with the get () method 
on the Query object:
"""

print "using get methode ==="
pariabel = query.get(1)
print pariabel.user_name
pariabel = query.get(2)
print pariabel.user_name

"""
If we want to filter the results retrieved by the Query object, we can use the filter ( )
and filter_by ( ) methods:
"""
print "using filter_by======"
for user in query.filter_by(display_name='Rick Copeland'):
    print user.id, user.user_name, user.password
print "using_filter =========="    
for user in query.filter(User.user_name.like('rick%')):
    print user.id, user.user_name, user.password
    
"""
To insert objects into the database, we simply create an object in Python and then use
the add( ) method to notify the session about the object:
"""
print "insert"
newuser = User()
newuser.user_name = "Ef"
newuser.password = "password"
newuser.display_name = "Michael"
#session.save(newuser) <-- tampaknya sudah gak bisa dipakai, penggantinya adalah session.add()
session.add(newuser)
#untuk merekan ke session digunakan fungsi commit()
session.commit()
#ubah display_name id 1 ke Richard
rick = query.get(1)
rick.display_name = 'Richard'
"""
fungsi add dan commit hanya menyimpan di session saja, data belum tersimpan ke database
untuk menyimpan ke database digunakan session.flush
"""
session.flush()

list(query)
for user in query:
    print user.user_name, user.password, user.display_name
    
