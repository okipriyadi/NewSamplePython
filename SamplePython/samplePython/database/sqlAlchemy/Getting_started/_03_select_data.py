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
To select data back out of the table, we can use the table's select ( ) method as follows:
"""

#ini untuk menampikan seluruh kolom
stmt = user_table.select()
result = stmt.execute()
for row in result:
    print row

#cara ke dua
print "cara kedua================="
stmt3 = select([user_table])
for row in stmt3.execute():
    print row


#ini untuk menampikan hanya kolom username
print "menampilkan hanya kolom username================="
stmt2 = select([user_table.c.user_name])
for row in stmt2.execute():
    print row

"""
We can also retrieve values from each row of the result using dict -like indexing or
simple attribute lookup as follows:
"""
print "print masing-masing row ============"
result2 = stmt.execute()
row = result2.fetchone()
print row['user_name']
print row.user_name
print row['password']
print row.password
print row['created']
print row.created
print row.items()
print row.keys()
print row.values()
print row.has_key('user_name')
print row.has_key('msrp')

"""
To restrict the rows that are returned from the select ( ) method, we can supply a where
clause. SQLAlchemy provides a powerful SQL expression language to assist in the
construction of where clauses, as shown in the following example:
"""


print "menggunakan where (menampilkan hanya user_name == rick =================)"
stmt = user_table.select(user_table.c.user_name=='rick')
print stmt.execute().fetchall()


"""
The actual parameters used by select ( ) are listed next. They are discussed in more
detail later in the chapter.
columns = None
A list of ClauseElement structures to be returned from the query.
bind = None
An engine on a connectable object on which to execute the statement. If this is
omitted, an engine binding will be inferred from referenced columns and/or tables,
if possible.
whereclause = None
A ClauseElement expression used to for the WHERE clause.
from_obj = []
A list of Table s or other selectable objects that will be used to form the FROM
clause. If this is not specified, the FROM clause is inferred from the tables refer-
enced in other clauses.
order_by = None
A list of ClauseElement s used to construct the ORDER BY clause.
group_by = None
A list of ClauseElement s used to construct the GROUP BY clause.
having = None
A ClauseElement used to construct the HAVING clause.
distinct = False
Adds a DISTINCT qualifier to the column list in the SELECT statement.
for_update = False
Adds a FOR UPDATE qualifier to the SELECT statement. Some databases support
other values for this parameter, such as MySQL, which supports "read" (translating
to LOCK IN SHARE MODE), or Oracle, which supports "nowait" (translating to
FOR UPDATE NOWAIT).
limit = None
The numerical limit for the number of rows returned. Typically this uses the LIMIT
clause, but SQLAlchemy provides some support for LIMIT even when the under-
lying database does not support it directly.
offset = None
The numerical offset for the starting row that is returned. Typically this uses the
OFFSET clause, but SQLAlchemy provides some support for OFFSET even when
the underlying database does not support it directly.
correlate = True
Indicates that this SELECT statement is to be "correlated" with its enclosing SE-
LECT statement if it is used as a subquery. In particular, any selectables present in
both this statement's from_obj list and the enclosing statement's from_obj list will
be omitted from this statement's FROM clause.
use_labels = False
Generates unique labels for each column in the columns list, to ensure there are no
name collisions.
prefixes = None
A list of ClauseElement s to be included directly after the SELECT keyword in the
generated SQL. This is used for dialect-specific SQL extensions, to insert text be-
tween the SELECT keyword and the column list.
Result set objects
Thus far, we have glossed over the return value of the execute ( ) method on SQL state-
ments, showing only that it is possible to iterate over this value and receive tuple-like
objects. In fact, SQLAlchemy provides an object, defined in the ResultProxy class, to
allow cursor-like access to the results of a query. Some of the useful methods and at-
tributes available on the ResultProxy object are summarized next.
fetchone ( )
Fetch one result from the cursor.
fetchmany ( size = None )
Fetch several results from the cursor (if size is omitted, fetch all results).
fetchall ( )
Fetch all results from the cursor.
__iter__ ( )
Return an iterator through the result set.
close ( )
Close the ResultProxy , as well as the underlying cursor. This method is called au-
tomatically when all result rows are exhausted.
scalar ( )
Fetch the first column of the first row, and close the result set (useful for queries
such as "SELECT DATETIME('NOW')").
rowcount (valid only for DML statements)
Return the number of rows updated, deleted, or inserted by the statement.
The "rows" returned from a ResultProxy object, either via the fetch* ( ) methods or
iteration, is actually a RowProxy object. As we have seen previously, it supports a tuple-
like interface. We can also retrieve columns from the RowProxy object through its dict -
like interface or its object -like interface:
"""
