import os.path
import json
from ..library.SQLiteDriver import SQLiteDriver

class PhonebookModel(SQLiteDriver):

	def __init__(self):
		SQLiteDriver.__init__(self)
