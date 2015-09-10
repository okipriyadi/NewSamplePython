"""
As mentioned previously, MetaData can be bound to a database Engine . This is done in
one of three ways:
• Specify the Engine URI in the MetaData constructor
• Specify an actual Engine or other Connectable object in the MetaData constructor
• Assign the bind attribute of an “unbound” MetaData to an Engine or other Connect
able
The various ways of binding MetaData are illustrated in the following examples:
"""
from sqlalchemy import *
# Create a bound MetaData with an implicitly created engine
bound_meta2 = MetaData('sqlite:///test2.db')
# Create an engine and then a bound MetaData
db2 = MetaData('sqlite:///test1.db')
bound_meta1 = MetaData(db2)
# Create an unbound MetaData
unbound_meta = MetaData()
# Create an Engine and bind the MetaData to it
db1 = create_engine('sqlite://')
unbound_meta.bind = db1

"""
Binding the MetaData object to an engine allows the MetaData and the objects attached
to it ( Table s, Index es, Sequence s, etc.) to perform database operations without explicitly
specifying an Engine :
"""
from sqlalchemy import *
metadata = MetaData('sqlite://')
user_table = Table('tf_user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_name', Unicode(16), unique=True, nullable=False,index=True),
                   Column('password', Unicode(40), nullable=False),
                   Column('first_name', Unicode(255), default=''),
                   Column('last_name', Unicode(255), default='', index=True))
user_table.create()
# we can omit the bind parameter