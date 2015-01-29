class Schema(object):

	@staticmethod
	def tablePerson():
		return "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT NOT NULL, alamat TEXT NOT NULL)"

	@staticmethod
	def tablePhonebook():
		return "CREATE TABLE IF NOT EXISTS phonebook(id INTEGER PRIMARY KEY AUTOINCREMENT, person_id INTEGER NOT NULL, phone TEXT NOT NULL)"

	@staticmethod
	def tableRelation():
		return "CREATE TABLE IF NOT EXISTS relation(id INTEGER PRIMARY KEY AUTOINCREMENT, phonebook_id INTEGER NOT NULL, person_id INTEGER NOT NULL, relation TEXT NOT NULL)"
