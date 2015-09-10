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


stmt = user_table.select()
result = stmt.execute()
for row in result:
    print row


# Create an update constrained by user name
stmt_update = user_table.update(user_table.c.user_name=='rick')
# Execute the update, setting the password column to secret123
stmt_update.execute(password='secret1234')
print "after update ==============="
result = stmt.execute()
for row in result:
    print row

# Create a delete statement that deletes all users except for 'rick'

stmt_delete = user_table.delete(user_table.c.user_name != 'rick')
stmt_delete.execute()
print "after delete ============"
result = stmt.execute()
for row in result:
    print row
