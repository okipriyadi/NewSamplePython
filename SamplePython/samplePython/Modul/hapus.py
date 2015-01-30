from sqlalchemy import *
from sqlalchemy.orm import backref, mapper, relation
from sqlalchemy.orm import sessionmaker, create_session

db = create_engine('sqlite:///joindemo.db')

db.echo = True

metadata = MetaData(bind=db)

users = Table('users', metadata, autoload=True)
emails = Table('emails', metadata, autoload=True)

# These are the empty classes that will become our data classes
class User(object):
    pass
class Email(object):
    pass

usermapper = mapper(User, users)
emailmapper = mapper(Email, emails)

session = create_session()

mary = session.query(User).filter(users.c.name=='Mary').first()
mary.age += 1

session.commit()

fred = User()
fred.name = 'Fred'
fred.age = 37

print "About to flush() without a save()..."
session.flush()  # Will *not* save Fred's data yet

session.save(fred)
print "Just called save(). Now flush() will actually do something."
session.flush()  # Now Fred's data will be saved

session.delete(fred)
session.flush()