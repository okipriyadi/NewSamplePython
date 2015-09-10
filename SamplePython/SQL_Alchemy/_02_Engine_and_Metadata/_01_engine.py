"""
The SQLAlchemy-provided Engine class is responsible for managing the connection to
the database. It does this by incorporating a database connection pool and a database-
specific Dialect layer to translate the SQL expression language (chapter 5) into
database-specific SQL.
To get started using an Engine , you use the create_engine( ) function:
"""
from sqlalchemy import *
# Create a connection to a SQLite in-memory database
#engine = create_engine('sqlite://')
# Create a connection to a SQLite on-disk database "data.sqlite"
engine = create_engine('sqlite:///data.sqlite')
# Create a connection to a PostGreSQL database
#engine = create_engine('postgres://rick:foo@localhost:5432/pg_db')
# Create a connection to a MySQL database
#engine = create_engine('mysql://localhost/mysql_db')
# Create a connection to an Oracle database (via TNS)
#engine = create_engine('oracle://rick:foo@oracle_tns')
# Create a connection to an Oracle database (without a TNS name)
#engine = create_engine('oracle://rick:foo@localhost:1521/oracle_sid')

"""
The first argument to create_engine ( ) is the RFC-1738 style URL specifying the data-
base. The general form of the url is: driver :// username : password @ host : port / database .

Of course, the various database drivers interpret these URLs in slightly different ways,
as illustrated here. It is also possible to pass additional arguments to the low-level DB-
API driver created by SQLAlchemy via either a URL query string:
"""

#url='postgres://rick:foo@localhost/pg_db?arg1=foo&arg2=bar'
#engine = create_engine(url)

"""
or via the connect_args parameter to create_engine ( ):
"""
engine = create_engine('postgres://rick:foo@localhost/pg_db',
                        connect_args=dict(arg1='foo', arg2='bar'))
"""
If you wish complete control over the connection creation process, you can even pass
a function (or other callable object) that returns a DB-API connection to create_engine (
) in the creator argument:
"""

import psycopg
def connect_pg():
    return psycopg.connect(user='rick', host='localhost')
engine = create_engine('postgres://', creator=connect_pg)

"""
The full set of keyword arguments accepted by create_engine ( ) are specified in here:
connect_args : A dictionary of options to be passed to the DBAPI’s connect( ) method. The default
is {}. 

convert_unicode : Indicates whether the engine should convert all unicode values into raw byte strings
before going into the database, and convert raw byte strings to unicode coming
out of result sets. This can be useful, for instance, when dealing with a database
server or schema that does not provide unicode support natively. The default is False.

creator  : A callable that returns a DB-API connection. The default is None.

echo     : A flag that tells SQLAlchemy to echo all statements and bind parameter values to
its logger. The default is None. 

echo_pool : A flag that tells SQLAlchemy to log all connection pool checkins and checkouts.
The default is False.

encoding : Specifies the encoding to use in all translations between raw byte strings and Python
unicode objects. The default is False.

module  : Specifies which module to use when a database implementation can use more than
one (such as PostgreSQL and Oracle). The default is None.

pool    : Use an existing connection pool rather than creating a new one. The default is
None.

poolclass : If the engine is creating its own connection pool, the class (a subclass of sqlal
chemy.pool.Pool ) to use when constructing the pool object. If no pool class is
specified, sqlalchemy.pool.QueuePool will be used for all database drivers except
for SQLite, which uses the sqlalchemy.pool.SingletonThreadPool . The default is
None.

max_overflow : The number of connections to allow the connection pool to overflow to (only
applicable with the QueuePool ). The default is 10.

pool_size: The number of connections to keep alive in the connection pool (only applicable
to the QueuePool and SingletonThreadPool pool classes). The default is 5.

pool_recycle : Close and reopen connections after this number of seconds of inactivity, or, if -1
(the default), disable connection recycling. This is useful if the database server
times out connections after a period of inactivity, as MySQL does.

pool_timeout : The number of seconds to wait when getting a connection from the pool before
giving up, (applicable only to QueuePool connection pools). The default is 30.

strategy : Selects an alternate implementation of the engine; the only current strategies are
' plain ' and ' threadlocal ‘. ' threadlocal ' reuses connections for multiple statements
within a thread; ' plain ' (the default) uses a new connection for each statement.

threaded : Used only by cx_Oracle, makes the engine threadsafe. If this is not required, per-
formance might be improved by setting this parameter to False .

use_ansi : Used only by Oracle to correct for a quirk of Oracle versions 8 and earlier when
handling LEFT OUTER JOINs.

use_oids : Used only by PostgreSQL to enable the column name " oid " (object ID).
"""