"""
The basic way mapping that SQLAlchemy performs is useful, but what if we have a
property or function that conflicts with the way SQLAlchemy wants to map columns?
Or what if we just want to customize the columns mapped by SQLAlchemy? Fortu-
nately, SQLAlchemy provides a rich set of ways to customize the way properties are
mapped onto your classes.
"""
"""
================================================================================
Using include_properties and exclude_properties
================================================================================
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
                              Column('name', Unicode(255)),
                              Column('description', Unicode))

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
The simplest case is where we want to restrict the properties mapped. In this case, we
can use the include_properties to only map those columns specified:
"""
#dijadikan komentar dulu karna dibawah mappernya diganti biar gak tubrukan
#print dir(Region)
#mapper(Region, region_table, include_properties=['id'])
#print dir(Region)

"""
We can also use exclude_properties to specify columns to be excluded:
"""
print dir(Level)
mapper(Level, level_table, exclude_properties=['name'])
print dir(Level)

"""
If we want to map all the columns to properties with a particular prefix, we can use the
column_prefix keyword argument:
"""
print "=========column_prefix==========="
#print dir(Region)
#mapper(Region, region_table, column_prefix='_')
#print dir(Region)

"""
kita juga dapat mengubah nama mapped dari kolom-ke kolom menggunakan properties parameter
We can also customize the mapped property names on a column-by-column basis using
the properties parameter:
"""
print "=========properties==========="
mapper(Region, region_table, properties=dict(region_name=region_table.c.name,region_id=region_table.c.id))
print dir(Region)

"""
kadang kala kita butuh untuk membuat sebuah properti yang menkombinasikan beberapa kolom atau juga hasil dari subquery. 
untuk itu kita gunakan fungsi column_property()
"""
print "=========column_properties==========="
average_price = select([func.avg(product_price_table.c.price)],
                       product_price_table.c.sku==product_table.c.sku).as_scalar().label('average_price')
print "average_price =", average_price, "\n ============="

mapper(Product, product_table, properties=dict( average_price=column_property(average_price)))
metadata.bind.echo = True
Session = sessionmaker()
session = Session()
p = session.query(Product).get('123')
print p.sku, p.msrp, p.average_price

"""
SQL Alchemy juga menyediakan pembuatan properti dari grup beberapa kolom, 
untuk menggunakannya kita buat custom class untuk menyimpan gabungan hasil.
class tersebut harus mmpunyai sebuah konstruktor yang mampu menerima kolom hasil sebagai 
positional argumen dan sebuah method __composite_values__()yang mengembalikan sebuah list atau tuple yang 
merepresentasikan keaadaan objek . class tersebut juga harus mensupport perbandingan via 
__eq__() __ne__() methods.

 
For instance, suppose we have a mapping database that stores route segments in the
following table:
"""
segment_table = Table( 'segment', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('lat0', Float),
                       Column('long0', Float),
                       Column('lat1', Float),
                       Column('long1', Float))
"""
In this case, our application expects RouteSegment s to have a beginning and an ending
MapPoint object, defined as follows:
"""

class RouteSegment(object):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
    def __repr__(self):
        return '<Route %s to %s>' % (self.begin, self.end)
    
class MapPoint(object):
    def __init__(self, lat, long):
        self.coords = lat, long
    
    def __composite_values__(self):
        return self.coords
    
    def __eq__(self, other):
        return self.coords == other.coords
    
    def __ne__(self, other):
        return self.coords != other.coords
    
    def __repr__(self):
        return '(%s lat, %s long)' % self.coords
    
"""
We can then map the class and use it with the composite ( ) function:
"""
mapper(RouteSegment, segment_table, 
       properties=dict(begin=composite(MapPoint, 
                                       segment_table.c.lat0,
                                       segment_table.c.long0
                                       ),
                       end=composite(MapPoint,
                                     segment_table.c.lat1, segment_table.c.long1
                                     )
                       )
       )

work=MapPoint(33.775562,-84.29478)
library=MapPoint(34.004313,-84.452062)
park=MapPoint(33.776868,-84.389785)
routes = [
          RouteSegment(work, library),
          RouteSegment(work, park),
          RouteSegment(library, work),
          RouteSegment(library, park),
          RouteSegment(park, library),
          RouteSegment(park, work)]
for rs in routes:
    session.add(rs)
    session.commit()
    session.flush()
q = session.query(RouteSegment)
print RouteSegment.begin==work
q = q.filter(RouteSegment.begin==work)
for rs in q:
    print rs