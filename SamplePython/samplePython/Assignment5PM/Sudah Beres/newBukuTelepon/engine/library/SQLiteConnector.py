
import sqlite3 as lite

class SQLiteConnector(object):
	database = 'files/database.db'
	instance = None

	@staticmethod
	def getInstance():
		if(SQLiteConnector.instance==None):
			SQLiteConnector.instance = lite.connect(SQLiteConnector.database)
		return SQLiteConnector.instance
