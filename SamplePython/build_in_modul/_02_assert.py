"""
Python's assert statement helps you find bugs more quickly 
"""


class MyDB:
    def __init__(self):
        self._id2name_map = {}
        self._name2id_map = {}
    
    def add(self, id, name):
        self._name2id_map[name] = id
        self._id2name_map[id] = name
    
    def by_name(self, name):
        return self._name2id_map[name]
    
"""
One of the "invariants" of this class is that the name2id_map ought to always be in the inverse 
of the id2name_map. You can see that the add() function tries to enforce that. 
However, it's possible that this invariant will be broken at some point: 
perhaps there is a typo in one of the methods, or perhaps some other bit of code gets in and fiddles 
with the private variables, etc. Perhaps it only happens for some values.

A good place to add assertions to this class would be to check that the data-structure invariants are correct. For example

def by_name(self, name):
   id = self._name2id_map[name]
   assert self._id2name_map[id] == name
   return id
"""





"""
Assertions are particularly useful in Python because of Python's powerful and flexible dynamic 
typing system. In the same example, we might want to make sure that ids are always numeric: 
this will protect against internal bugs, and also against the likely case of somebody 
getting confused and calling by_name when they meant by_id.

example:

from types import *
class MyDB:
    ...
    def add(self, id, name):
        assert type(id) is IntType, "id is not an integer: %r" % id
        assert type(name) is StringType, "name is not a string: %r" % name
"""
