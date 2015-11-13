"""
Creating a database with peewee is extremely easy. In fact, it's easier to create the 
database in peewee than it is in SQLAlchemy. All you need to do is call 
peewee's SqliteDatabase method and pass it the path of the file or 
":memory:" if you want an in-memory database.  Let's create a database to hold information 
about our music collection. We'll create two tables: Artist and Album.
"""

# models.py
import peewee
 
database = peewee.SqliteDatabase("wee.db")
 
########################################################################
class Artist(peewee.Model):
    """
    ORM model of the Artist table
    """
    name = peewee.CharField()
 
    class Meta:
        database = database
 
########################################################################
class Album(peewee.Model):
    """
    ORM model of album table
    """
    artist = peewee.ForeignKeyField(Artist)
    title = peewee.CharField()
    release_date = peewee.DateTimeField()
    publisher = peewee.CharField()
    media_type = peewee.CharField()
 
    class Meta:
        database = database
 
 
if __name__ == "__main__":
    try:
        Artist.create_table()
    except peewee.OperationalError:
        print "Artist table already exists!"
 
    try:
        Album.create_table()
    except peewee.OperationalError:
        print "Album table already exists!"