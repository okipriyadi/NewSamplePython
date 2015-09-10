"""
The most common use of the MetaData object is in defining the tables in your schema.
In order to define tables in the MetaData , you use the Table and Column classes as shown
in the following example:
"""
from sqlalchemy import *
from datetime import datetime
metadata=MetaData()
user_table = Table(
                   'tf_user', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('user_name', Unicode(16), unique=True, nullable=False),
                   Column('email_address', Unicode(255), unique=True, nullable=False),
                   Column('password', Unicode(40), nullable=False),
                   Column('first_name', Unicode(255), default=''),
                   Column('last_name', Unicode(255), default=''),
                   Column('created', DateTime, default=datetime.now))

"""
Unlike some other database mapping libraries, SQLAlchemy fully supports the use of
composite and non-integer primary and foreign keys:
"""

brand_table = Table( 'brand', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', Unicode(255), unique=True, nullable=False))

product_table = Table('product', metadata,
                      Column('brand_id', Integer, ForeignKey('brand.id'),primary_key=True),
                      Column('sku', Unicode(80), primary_key=True))

style_table = Table('style', metadata,
                    Column('brand_id', Integer, primary_key=True),
                    Column('sku', Unicode(80), primary_key=True),
                    Column('code', Unicode(80), primary_key=True),
                    ForeignKeyConstraint(['brand_id', 'sku'], ['product.brand_id','product.sku']))
