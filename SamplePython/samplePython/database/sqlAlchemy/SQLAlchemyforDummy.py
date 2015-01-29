from sqlalchemy import *
from sqlalchemy.orm import *
from datetime import datetime

db = create_engine('sqlite:///tutorial.sqlite')

db.echo = False  

metadata = MetaData('sqlite:///tutorial.sqlite')

user_table = Table(
    'tf_user', metadata,
        Column('id', Integer, primary_key=True),
        Column('user_name', Unicode(16),unique=True, nullable=False),
        Column('password', Unicode(40), nullable=False),
        Column('display_name', Unicode(255)),
        Column('created', DateTime, default=datetime.now))

group_table = Table(
    'tf_group', metadata,
        Column('id', Integer, primary_key=True),
        Column('group_name', Unicode(16), unique=True, nullable=False))

permission_table = Table(
    'tf_permission', metadata,
        Column('id', Integer, primary_key=True),
        Column('permission_name', Unicode(16),unique=True, nullable=False))

#Create relation table many to many between user_tabel & Group
user_group_table = Table(
    'tf_user_group', metadata,
        Column('user_id', None, ForeignKey('tf_user.id'),primary_key=True),
        Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True))

#Create relation table many to many between Table Group & permission 
group_permission_table = Table(
    'tf_group_permission', metadata,
        Column('permission_id', None, ForeignKey('tf_permission.id'), primary_key=True),
        Column('group_id', None, ForeignKey('tf_group.id'), primary_key=True))

metadata.create_all()
#stmt = user_table.insert()
#stmt.execute(user_name='rick', password='secret',display_name='Rick Copeland')
#stmt.execute(user_name='rick1', password='secret',display_name='Rick Copeland Clone')

stmt = user_table.select()
result = stmt.execute()
for row in result:
    print row

print "\n u can also print like this"
result = stmt.execute()
row =result.fetchone()
print "username : ", row['user_name']
print "passwor: ",  row.password
print "created: ", row.created
print row.items()


"""
print "Using Select"
stmt = user_table.select(user_table.c.user_name=='rick')
print stmt.execute().fetchall()


print "Create an update constrained by user name"
bazar = user_table.update(user_table.c.user_name=='rick')
print bazar.execute(password='secret123')
"""

class User(object): pass
class Group(object): pass
class Permission(object): pass
mapper(User, user_table)
mapper(Group, group_table)
mapper(Permission, permission_table)
print "=============using ORM"
#kelas
Session = sessionmaker()
#Objek
session = Session()
#we use it to obtain access to a Query object for our class
query = session.query(User)
#The simplest way to use the Query object is as an iterator for all the objects in thedatabase
print list(query)
for user in query:
    print user.user_name
#We can also retrieve an object from the database by using its primary key
print query.get(1)

#Filter_by

"""
for user in query.filter_by(display_name='Rick Copeland'):
    print user.id, user.user_name, user.password

#Filter
for user in query.filter(User.c.user_name.like('rick%')):
    print user.id, user.user_name, user.password
"""
