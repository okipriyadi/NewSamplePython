from sqlalchemy import *
from datetime import datetime

"""
Untuk konek ke database, kita akan membuat sebuah MetaData object, yang akan digunakan oleh 
SQLAlchemy untuk terus men-track tabel yang telah kita definisikan.

Object MetaData yang kita buat terikat ke sebuah engine database tertentu , dalam hal ini
SQLite engine tekoneksi ke database yang berlokasi di file tutorial.sqlite. 
Jika tutorial.sqlite tidak ada, maka tutorial.sqlite akan dibuat secara otomatis oleh SQLite.

"""

metadata = MetaData('sqlite:///tutorial.sqlite')

#setelah kita membuat MetaData , kita dapat mendefinisikan tabel.


user_table = Table('tf_user', metadata,
                   Column('id', Integer, primary_key = True), 
                   Column('user_name', String(16), unique=True, nullable=False),
                   Column('password', String(40), nullable=False),
                   Column('display_name', String(40), default=''),
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

"""
Finally, we define the join tables that provide a many-to-many relationship between
users and groups and groups and permission
"""

user_group_table = Table('tf_user_group', metadata,
                         Column('user_id', None, ForeignKey('tf_user.id'), primary_key=True),
                         Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True)
                         )

group_permission_table = Table('tf_group_permission', metadata, 
                            Column('permission_id', None, ForeignKey('tf_permission.id'), primary_key=True),
                            Column('group_id', None, ForeignKey('tf_group.id'),primary_key=True)
                           )
"""
Once the tables have been defined, we can create them in the database using the fol-
lowing code:
"""
metadata.create_all()
"""
If you were not creating the database, but rather connecting to an existing database,
you could, of course, leave out the call to metadata.create_all ( ). SQLAlchemy will in
any case create tables using the IF NOT EXISTS syntax, so a metadata.create_all ( ) is a
safe operation.
"""
