"""
SQLAlchemy provides the connection pool as an easy and efficient way to manage
connections through the database. Normally, you don’t need to worry about 
the connection pool, because it is automatically managed by the Engine class. 
The connection pool can, however, be used on its own to manage regular DB-API connections. 
If you wish to manage such a pool, you could do the following:
"""

from sqlalchemy import pool
import psycopg2

psycopg = pool.manage(psycopg2)
connection = psycopg.connect(database='mydb', username='rick', password='foo')

"""
The pool.manage () call sets up a connection pool (the exact object is an instance of
sqlalchemy.pool.DBProxy ). The connect ( ) method then works just as the Engine ’s
connect () method, returning a proxy for the DB-API connection from the managed
connection pool. When the connection proxy is garbage collected, the underlying DB-
API connection is returned to the connection pool.
By default, the connect () method returns the same connection object if it is called
multiple times in a given thread (the same “threadlocal” strategy used by the Engine ).
To specify that the pool should generate a new connection each time that connect ( ) is
called, pass use_threadlocal=False to the pool.manage ( ) function.
If you wish to use a particular connection pool class instead of the DBProxy as shown
previously, SQLAlchemy provides the ability to directly instantiate the pool:
"""
from sqlalchemy import pool
import psycopg2
import sqlite
def getconn_pg():
    c = psycopg2.connect(database='mydb', username='rick',password='foo')
    return c
def getconn_sl():
    c = sqlite.connect(filename='devdata.sqlite')
    return c

pool_pg = pool.QueuePool(getconn_pg, use_threadlocal=True)
# SQLite requires use of the SingletonThreadPool
pool_sl = pool.SingletonThreadPool(getconn_sl)

"""
Some of the various pool types that are available in the sqlalchemy.pool module are:

AssertionPool
Allows only one connection to be checked out at a time and raises an AssertionEr
ror when this constraint is violated.

NullPool
Does no pooling; instead, actually opens and closes the underlying DB-API con-
nection on each check out/check in of a connection.

QueuePool
Maintains a fixed-size connection pool. This is the default connection pool class
used for non-sqlite connections.

SingletonThreadPool
Maintains a single connection per thread. It is used with sqlite because this data-
base driver does not handle using a single connection in multiple threads well.

StaticPool
Maintains a single connection that is returned for all connection requests.


"""

