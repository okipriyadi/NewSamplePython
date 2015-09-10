"""
SQLAlchemy uses the Python standard library logging module to log various actions.
The echo and echo_pool arguments to create_engine ( ) and the echo_uow flag used on
Session objects all affect the regular loggers.

One useful debugging strategy is to add a logfile for a particular class of operations that
SQLAlchemy is performing. For instance, to capture all of the engine-related opera-
tions, we could set up the logger as follows:
"""
import logging
handler = logging.FileHandler('sqlalchemy.engine.log')
handler.level = logging.DEBUG
logging.getLogger('sqlalchemy.engine').addHandler(handler)

"""
The loggers used with SQLAlchemy are listed next. Note that several of these loggers
deal with material covered in later chapters (in particular, the sqlalchemy.orm.* log-
gers):

• sqlalchemy.engine -- control SQL echoing. logging.INFO logs SQL query output,
logging.DEBUG logs result sets as well.
• sqlalchemy.pool -- control connection pool logging. logging.INFO logs checkins
and checkouts.
• sqlalchemy.orm -- control logging of ORM functions. logging.INFO logs configu-
rations and unit of work dumps.
— sqlalchemy.orm.attributes -- Logs instrumented attribute operations.
— sqlalchemy.orm.mapper -- Logs mapper configurations and operations.
— sqlalchemy.orm.unitofwork -- Logs unit of work operations, including depend-
ency graphs.
— s qlalchemy.orm.strategies -- Logs relation loader operations (lazy and eager
loads).
— sqlalchemy.orm.sync -- Logs synchronization of attributes from one object to
another during a flush.
"""


