import sqlite3
    


class PhonebookModel:
    def __init__(self):
        self.con = sqlite3.connect('files/test.db')
        self.cur = self.con.cursor()
        
    def createTable(self):
        self.cur.execute('''CREATE TABLE person
        (id_person INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT , address TEXT)''')
        self.cur.execute('''CREATE TABLE phonebook
        (id_phonebook INTEGER PRIMARY KEY AUTOINCREMENT, id_person INTEGER , no_telp TEXT, FOREIGN KEY (id_person) REFERENCES person(id_person))''')
        self.cur.execute('''CREATE TABLE relation
        (id_relation INTEGER PRIMARY KEY ,id_person1 INTEGER, id_person2 INTEGER, relation TEXT)''')
        self.con.commit()
    
    def addPhonebook(self, name, address, listNumber):
        #self.createTable()
        self.cur.execute('''INSERT INTO person(name, address)
        VALUES(?,?)''',(name, address))
        self.con.commit()
        query = "select id_person from person where name ='" +name+"' AND address='"+address+"'"
        self.cur.execute(query)
        id_person = self.cur
        id_person2 = 0
        for i in id_person:
            for j in i:
                id_person2 = j
        for noTelp in listNumber:
            self.cur.execute('''INSERT INTO phonebook(id_person, no_telp)
            VALUES(?,?)''',(id_person2, noTelp))
            self.con.commit()
        
    def addRelationship(self, id1, id2, relation):
        self.cur.execute('''INSERT INTO relation(id_person1, idperson2, relation)
        VALUES(?,?,?)''',(id1, id2, relation))
        self.con.commit()
        
    def search(self, keyword):
        self.cur.execute(keyword)
        return self.cur
                        
        
 

#createTable()
#addPhonebook('OKi', 'cipedes',["085220902022"])


#cur.execute('SELECT * FROM phonebook')

#for i in cur:
    #print "\n"
    #for j in i:
        #print j
    
#data = cur.fetchone()
#print "SQLite version: %s" % data   