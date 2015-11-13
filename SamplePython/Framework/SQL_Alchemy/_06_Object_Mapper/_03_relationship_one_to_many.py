"""
To model each type of relationship, SQLAlchemy uses the relation ( ) function in the
properties dict of the mapper. dalam kebanyakan kasus, SQLAlchemy dapat menduga the proper
join condition for 1:N relations. 

For instance, since the stores in our data model are
members of regions (a 1:N relationship region:store), we can model this on our
Region class as follows:
"""

from sqlalchemy import *
from sqlalchemy.orm import *
metadata = MetaData('sqlite:///tutorial.sqlite')
 
level_table = Table( 'level', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('parent_id', None, ForeignKey('level.id')),
                     Column('name', String(20))
                    )

category_table = Table('category', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('level_id', None, ForeignKey('level.id')),
                       Column('parent_id', None, ForeignKey('category.id')),
                       Column('name', String(20)))

product_table = Table('product', metadata,
                      Column('sku', String(20), primary_key=True),
                      Column('msrp', Numeric))

product_summary_table = Table('product_summary', metadata,
                              Column('sku', None, ForeignKey('product.sku'), primary_key=True),
                              Column('name', String(255)),
                              Column('description', String))

product_category_table = Table('product_category', metadata,
                               Column('product_id', None, ForeignKey('product.sku'), primary_key=True),
                               Column('category_id', None, ForeignKey('category.id'), primary_key=True))

region_table = Table('region', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(255)))

store_table = Table('store', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('region_id', None, ForeignKey('region.id')),
                    Column('name', String(255)))

product_price_table = Table('product_price', metadata,
                            Column('sku', None, ForeignKey('product.sku'), primary_key=True),
                            Column('store_id', None, ForeignKey('store.id'), primary_key=True),
                            Column('price', Numeric, default=0)
                            )

 
metadata.create_all()

class Level(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
    def __repr__(self):
        return '<Level %s>' % self.name

class Category(object):
    def __init__(self, name, level, parent=None):
        self.name = name
        self.level = level
        self.parent = parent
    def __repr__(self):
        return '<Category %s.%s>' % (self.level.name, self.name)

class Product(object):
    def __init__(self, sku, msrp, summary=None):
        self.sku = sku
        self.msrp = msrp
        self.summary = summary
        self.categories = []
        self.prices = []
    def __repr__(self):
        return '<Product %s>' % self.sku

class ProductSummary(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __repr__(self):
        return '<ProductSummary %s>' % self.name

class Region(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Region %s>' % self.name

class Store(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Store %s>' % self.name

class Price(object):
    def __init__(self, product, store, price):
        self.product = product
        self.store = store
        self.price = price
        
    def __repr__(self):
        return '<Price %s at %s for $%.2f>' % (self.product.sku, self.store.name, self.price)

"""
SQLAlchemy is able to infer the 1:N relation type by the foreign key relationship
between region_table and store_table .
"""
mapper(Store, store_table)
mapper(Region, region_table, properties=dict(stores=relation(Store)))

Session = sessionmaker()
session = Session()
metadata.bind.echo = True

"""
Adding a store to the region is as simple as appending on to the property. Generally,
when working at the ORM level, it is not necessary to worry about foreign keys. The
SELECT statement is necessary for SQLAlchemy to retrieve the inital contents of
the "stores" property.
"""
rgn = session.query(Region).get(1)
print "rgn ===", rgn.name
s0 = Store(name='3rd and Juniper')
rgn.stores.append(s0)

"""
SQLAlchemy automatically infers that a new store must be inserted with the
region_id properly set.
"""
session.commit()
session.flush()    

"""
In some cases, SQLAlchemy is unable to infer the proper join condition (for instance,
when there are multiple foreign key relations between the two tables). In this case, we
can simply use the primaryjoin parameter to the relation ( ) function:

mapper(Region, region_table, properties=dict(stores=relation(Store,primaryjoin=(store_table.c.region_id
==region_table.c.id))))
"""

