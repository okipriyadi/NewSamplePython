"""
To create a new MetaData object, you simply call its constructor, possibly with infor-
mation about how to connect to the database. If the constructor is called with no
arguments, it is considered to be unbound; if it is called with either an Engine or a SQL
connection URI, it is considered bound. Shortcuts are available to bound MetaData and
to objects within a bound MetaData to facilitate the execution of statements against the
bound engine. Most of the time you will probably use a bound MetaData object. how-
ever, it is sometimes useful to use an unbound MetaData if you need to connect to
multiple database servers, where each server contains the same database schema.
The various ways to construct MetaData objects are illustrated in the following exam-
ples:
"""
from sqlalchemy import *
# create an unbound MetaData
unbound_meta = MetaData()
# create an Engine and bind the MetaData to it
db1 = create_engine('sqlite://')
unbound_meta.bind = db1
# Create an engine and then a bound MetaData
db2 = MetaData('sqlite:///test1.db')
bound_meta1 = MetaData(db2)
# Create a bound MetaData with an implicitly created engine
bound_meta2 = MetaData('sqlite:///test2.db')

"""
Note that you are never required to bind the MetaData object; all operations that rely
on a database connection can also be executed by passing the Engine explicitly as the
keyword parameter bind . This is referred to as explicit execution. If a MetaData instance
is bound, then the bind parameter can be omitted from method calls that rely on the
database connection. This is referred to as implicit execution. The “bound-ness” of a
MetaData object is shared by all Table s, Index es, and Sequence s in the MetaData , so a
Table attached to a bound MetaData , for instance, would be able to create itself via:
table.create()
whereas a Table in an unbound MetaData would need to supply a bind parameter:
table.create(bind=some_engine_or_connection)
"""
