"""
In order to use the SQLAlchemy ORM, we need three things: 
1. a database schema defined on a MetaData object, 
2. an object model (no special preparation of the object model is required for use by SQLAlchemy), 
3. a mapper configuration. 
"""
from sqlalchemy.orm import *
from sqlalchemy import *
metadata = MetaData('sqlite:///tutorial.sqlite')

"""
===================================================================================
1. a database schema defined on a MetaData object
===================================================================================
"""

#This is a "level" used in categorizing a product in a hierarchy. In our example, we will use the levels "Gender", "Department", "Class", and "Subclass"
level_table = Table( 'level', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('parent_id', None, ForeignKey('level.id')),
                     Column('name', String(20))
                    )

#These are the individual categories within a level. In our example, for instance, within the "Gender" level, we have "Men", "Women", "Children", and "Unisex.
category_table = Table('category', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('level_id', None, ForeignKey('level.id')),
                       Column('parent_id', None, ForeignKey('category.id')),
                       Column('name', String(20)))

product_table = Table('product', metadata,
                      Column('sku', String(20), primary_key=True),
                      Column('msrp', Numeric))

#This table contains auxilliary information about products that may or may not be present for each product.
product_summary_table = Table('product_summary', metadata,
                              Column('sku', None, ForeignKey('product.sku'), primary_key=True),
                              Column('name', Unicode(255)),
                              Column('description', Unicode))

#This table links the product table with the category table. A product should generally have one category per level.
product_category_table = Table('product_category', metadata,
                               Column('product_id', None, ForeignKey('product.sku'), primary_key=True),
                               Column('category_id', None, ForeignKey('category.id'), primary_key=True))

region_table = Table('region', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(255)))

store_table = Table('store', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('region_id', None, ForeignKey('region.id')),
                    Column('name', Unicode(255)))

#This table lists the retail price for each product at each store location.
product_price_table = Table('product_price', metadata,
                            Column('sku', None, ForeignKey('product.sku'), primary_key=True),
                            Column('store_id', None, ForeignKey('store.id'), primary_key=True),
                            Column('price', Numeric, default=0)
                            )

 
metadata.create_all()
"""
===================================================================================
2. an object model (no special preparation of the object model is required for use by SQLAlchemy)
===================================================================================
"""


"""
The application object model in the following listing is extremely basic. In a real ap-
plication, the classes would probably have additional methods defined for performing
domain-specific operations.
"""

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
Now that we have the basic schema and object model in place, we can start exploring
how to map objects. The region_table is one of the simplest tables, so we will start
there. The following example demonstrates mapping the region_table to the Region
class, and also illustrates the alterations that SQLAlchemy performs on the Region class
during mapping:
"""
  

"""
===================================================================================
3. a mapper configuration.
===================================================================================
"""
print dir(Region)
mapper(Region, region_table)
print dir(Region)
print Region.id
print Region.name

r0 = Region(name="Northeast")
r1 = Region(name="Southwest")
print r0
print r1

"""
These objects can be loaded or saved to the database using a session object :
"""
Session = sessionmaker()
session = Session()

session.add(r0)
session.add(r1)
metadata.bind.echo = True
print r0.id
print r0.name
print r1.id
print r1.name

session.commit()
session.flush()
print r0.id
print r0.name
print r1.id
print r1.name
"""
Note how SQLAlchemy automatically inserted the store names we specified into the
database, and then populated the mapped id attribute based on the synthetic key value
generated by the database. We can also update mapped properties once an object has
been saved to the database:
"""
print "after change======"
r0.name = "NorthWEST"
session.commit()
session.flush
print r0.id
print r0.name

