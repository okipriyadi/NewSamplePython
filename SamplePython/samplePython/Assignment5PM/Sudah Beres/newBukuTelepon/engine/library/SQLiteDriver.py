from SQLiteConnector import SQLiteConnector
from Schema import Schema

class SQLiteDriver:
	conn = None
	cursor = None

	def __init__(self):
		self.conn = SQLiteConnector.getInstance()
		self.cursor = self.conn.cursor()
		self.initSchema()

	def initSchema(self):
		self.queryExec(Schema.tablePerson())
		self.queryExec(Schema.tablePhonebook())
		self.queryExec(Schema.tableRelation())

	def queryOne(self, query):
		res = self.cursor.execute(query)
		return res.fetchone()

	def query(self, query):
		res = self.cursor.execute(query)
		return res

	def queryExec(self, query):
		self.cursor.execute(query)
		self.conn.commit()

	def insertId(self):
		return self.cursor.lastrowid

	def __exit__(self, type, value, traceback):
		self.conn.close()
