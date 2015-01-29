class PhonebookView(object):

	@staticmethod
	def showListPerson(persons):
		print '\n====================== person list'
		for person in persons:
			print person['id']
		if persons.rowcount<=0:
			print '<tidak ada data person>'
		print '\n--add[1] edit[2] delete[3] exit[0]--'
		pilihan = raw_input("pilihan : ")
		return pilihan

	@staticmethod
	def formPerson():
		nama = raw_input('nama : ')
		alamat = raw_input('alamat : ')
		return {'nama': nama, 'alamat': alamat}
