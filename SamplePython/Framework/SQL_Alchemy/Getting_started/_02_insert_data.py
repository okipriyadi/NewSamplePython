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
metadata.create_all()


"""
Once we have defined the tables in our schema, we can insert some data. To create a
new user, we use SQLAlchemy to construct an INSERT statement using the following
syntax:
"""

stmt = user_table.insert()

"""
Once the insert statement has been created, it can be executed multiple times with
different values:

ada tiga cara untuk meng-insert value, ini salah satunya: (utk melihat cara lainnya silahkan buka contoh lain di folder ini)
"""
stmt.execute(user_name='rick', password='secret',display_name='Rick Copeland')
stmt.execute(user_name='rick1', password='secret',display_name='Rick Copeland Clone')

