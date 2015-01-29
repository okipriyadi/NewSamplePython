from ..view.phonebook import PhonebookView
from ..model.phonebook import PhonebookModel
from ..model.person import PersonModel
from ..model.relation import RelationModel

class PhonebookController:
	data = []

	def __init__(self):
		self.phonebook = PhonebookModel()
		self.person = PersonModel()
		self.relation = RelationModel()
		self.listPerson()

	def listPerson(self):
		persons = self.person.get()
		PhonebookView.showListPerson(persons)
