from ..view.PhonebookView import PhonebookView
from ..model.PhonebookModel import PhonebookModel

class PhonebookController:
    data = []
    cur = ""

    def __init__(self):
        self.phonebook = PhonebookModel()
        #self.phonebook.createTable()
        self.menu()
        

    def menu(self):
        pilihan = PhonebookView.menu()
        self.action(pilihan)
        if pilihan!='9':
            self.menu()
            
    def tampilkan(self, cur):
        for i in cur:
            print "\n"
            for j in i:
                print j
                
    def action(self, pilihan):
        if pilihan=='1':
            noTelp = []
            new = PhonebookView.form()
            i=1
            while i <= int(new['banyakTelp']):
                no = PhonebookView.formTelepon()
                noTelp.append(no)
                i = i +1
            self.phonebook.addPhonebook(new['nama'], new['alamat'], noTelp)
        if pilihan == '2':
            keywordPars = 'SELECT p.id_person, p.name, p.address, b.no_telp  FROM person AS p LEFT JOIN phonebook AS b ON p.id_person = b.id_person' 
            cur = self.phonebook.search(keywordPars)
            self.tampilkan(cur)
        if pilihan =='3':
            keyword =  PhonebookView.search()
            keywordPars = "SELECT p.id_person, p.name, p.address, b.no_telp  FROM person AS p LEFT JOIN phonebook AS b ON p.id_person = b.id_person WHERE p.name LIKE '"+ keyword +"' OR address LIKE '"+ keyword +"'"
            cur = self.phonebook.search(keywordPars)
            self.tampilkan(cur)         
        """if pilihan == '4':
            PhonebookView.search()
            keyword = PhonebookView.pilihEdit()
            keyword2 = phonebookview.elemenEdit()
            keywordPars = "SELECT p.id_person, p.name, p.address, b.no_telp  FROM person AS p LEFT JOIN phonebook AS b ON p.id_person = b.id_person WHERE p.name LIKE '"+ keyword[0] +"' OR address LIKE '"+ keyword[0] +"'"
            cur = self.Phonebook.search(keywordPars)"""
        if pilihan =='5':
            new = PhonebookView.formRelation()
            self.phonebook.addRelationship(new['id_person1'], new['id_person2'], new['relation'])
        if pilihan =='6':
            keywordPars = "SELECT p.id_person, p.name, p.address, b.relatioan  FROM person AS p LEFT JOIN relation AS b ON p.id_person = b.id_person WHERE p.name LIKE '"+ keyword +"' OR address LIKE '"+ keyword +"'"
            cur = self.phonebook.search(keywordPars)
            
            
                
                 
            
                
            
            
        