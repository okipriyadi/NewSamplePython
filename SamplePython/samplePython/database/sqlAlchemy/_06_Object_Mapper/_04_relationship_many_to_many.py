"""
It is often useful to model many-to-many (M:N) type relations between objects. In the
database, this is accomplished by the use of an association or join table. In the following
schema, the relation between the product_table and the category_table is a many-to-
many:"""

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
In SQLAlchemy, we can model this relationship with the relation ( ) function and the
secondary parameter: .
"""
mapper(Category, 
       category_table, 
       properties=dict(products=relation(Product, secondary=product_category_table)))

mapper(Product, 
       product_table, 
       properties=dict(categories=relation(Category,secondary=product_category_table)))

                                                 
                                                 
Session = sessionmaker()
session = Session()
metadata.bind.echo = True

session.query(Product).get('123').categories
#session.commit()
#session.flush()    


"""
As in the case of the 1:N join, we can also explicitly specify the join criteria by using
the primaryjoin (the join condition between the table being mapped and the join table)
and the secondaryjoin (the join condition between the join table and the table being
related to) parameters:
mapper(Category, category_table, properties=dict(
products=relation(Product, secondary=product_category_table,
primaryjoin=(product_category_table.c.category_id
== category_table.c.id),
secondaryjoin=(product_category_table.c.product_id
== product_table.c.sku))))
mapper(Product, product_table, properties=dict(
categories=relation(Category, secondary=product_category_table,
primaryjoin=(product_category_table.c.product_id
== product_table.c.sku),
secondaryjoin=(product_category_table.c.category_id
== category_table.c.id))))"""
