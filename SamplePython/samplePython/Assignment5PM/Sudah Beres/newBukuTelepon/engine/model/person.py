import os.path
import json
from ..library.SQLiteDriver import SQLiteDriver

class PersonModel(SQLiteDriver):
	table = 'person'

	def __init__(self):
		SQLiteDriver.__init__(self)

	def get(self, condition=None):
		q = 'SELECT * FROM ' + self.table + ' '
		if condition!=None:
			q += 'WHERE ' + condition
		return self.query(q)

	def getOne(self, condition=None):
		q = 'SELECT * FROM person '
		if condition!=None:
			q += 'WHERE ' + condition
		return self.queryOne(q)

	def insert(self, data):
		q = 'INSERT INTO ' + self.table + '(nama, alamat) VALUES(' + data + ')'
		self.queryExec(q)
		return insertId()

	def update(self, data, condition):
		q = 'UPDATE ' + self.table + ' SET ' + data + ' WHERE ' + condition
		self.queryExec(q)
