import os.path
import json
from ..library.SQLiteDriver import SQLiteDriver

class RelationModel(SQLiteDriver):

	def __init__(self):
		SQLiteDriver.__init__(self)
