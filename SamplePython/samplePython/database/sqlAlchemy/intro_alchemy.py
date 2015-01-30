from sqlalchemy import create_engine
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import Integer, String
 
# create a connection to a sqlite database
# turn echo on to see the auto-generated SQL
engine = create_engine('sqlite:///tutorial2.db',
                       echo=True)

# this is used to keep track of tables and their attributes 
metadata = MetaData(bind=engine)
 
users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(40)),
                    Column('age', Integer),
                    Column('password', String),
                    )
 
addresses_table = Table('addresses', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('user_id', None, ForeignKey('users.id')),
                        Column('email_address', String, nullable=False)                            
                        )
 
# create the table and tell it to create it in the 
# database engine that is passed
metadata.create_all()

print "cara pertama untuk insert"
# create an Insert object
ins = users_table.insert()
# add values to the Insert object
new_user = ins.values(name="Joe", age=20, password="pass")
 
# create a database connection
conn = engine.connect()
# add user to database by executing SQL
conn.execute(new_user)
print "Cara kedua untuk insert"
# a connectionless way to Insert a user
ins = users_table.insert()
result = engine.execute(ins, name="Shinji", age=15, password="nihongo")

print "cara ketiga"
# another connectionless Insert
result = users_table.insert().execute(name="Martha", age=45, password="dingbat")

conn.execute(users_table.insert(), [
    {"name": "Ted", "age":10, "password":"dink"},
    {"name": "Asahina", "age":25, "password":"nippon"},
    {"name": "Evan", "age":40, "password":"macaca"}
])


from sqlalchemy.sql import select
 
s = select([users_table])
result = s.execute()
print '%-4s%-20s%-35s' % ("No","Nama","Age") 
for row in result:
    
    print '%-4s%-20s%-35s' % (row[0], row[1], row[2])
    
# get all the results in a list of tuples
conn = engine.connect()
res = conn.execute(s)
rows = res.fetchall()
print rows

#And if you just need the first result back, then you use fetchone() instead of fetchall():
res = conn.execute(s)
row = res.fetchone()
print row

s = select([users_table.c.name, users_table.c.age])
result = conn.execute(s)
print '%-20s%-35s' % ("Nama","Age")
for row in result:
    print '%-20s%-35s' % (row[0], row[1])
    
from sqlalchemy.sql import and_
 
# The following is the equivalent to 
# SELECT * FROM users WHERE id > 3
s = select([users_table], users_table.c.id > 3)
result = conn.execute(s)
print '%-4s%-20s%-35s' % ("No","Nama","Age") 
for row in result:
    
    print '%-4s%-20s%-35s' % (row[0], row[1], row[2])

# You can use the "and_" module to AND multiple fields together
s = select([users_table], and_(users_table.c.name=="Martha", users_table.c.age > 25))
result = conn.execute(s)
print '%-4s%-20s%-35s' % ("No","Nama","Age") 
for row in result:
    
    print '%-4s%-20s%-35s' % (row[0], row[1], row[2])
    