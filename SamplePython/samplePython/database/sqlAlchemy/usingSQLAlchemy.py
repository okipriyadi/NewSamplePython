"""The following example represents an n-to-1 relationship between movies and their directors. 
It is shown how user-defined Python classes create corresponding database tables, 
how instances with relationships are created from either side of the relationship, 
and finally how the data can be queried—illustrating automatically-
generated SQL queries for both lazy and eager loading."""

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()
class Movie(Base):
    __tablename__ = 'movies'
 
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    year = Column(Integer)
    directed_by = Column(Integer, ForeignKey('directors.id'))
 
    director = relation("Director", backref='movies', lazy=False)
 
    def __init__(self, title=None, year=None):
        self.title = title
        self.year = year
 
    def __repr__(self):
        return "Movie(%r, %r, %r)" % (self.title, self.year, self.director)
 
class Director(Base):
    __tablename__ = 'directors'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
 
    def __init__(self, name=None):
        self.name = name
 
    def __repr__(self):
        return "Director(%r)" % (self.name)
 
engine = create_engine('dbms://user:pwd@host/dbname')
Base.metadata.create_all(engine)