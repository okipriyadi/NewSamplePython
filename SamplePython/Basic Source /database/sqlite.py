import sqlite3
con = sqlite3.connect('Toko.db',50)
# prepare a cursor object using cursor() method
cur = con.cursor()

#Query put Here
cur.execute('SELECT SQLITE_VERSION()')

# Fetch a single row using fetchone() method.
data = cur.fetchone()

#print the data
print "SQLite version: %s" % data

#Create Table
def CreateTable():
    cur.execute('''CREATE TABLE Customers
    (CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, CustomerName TEXT, ContactName TEXT, Address TEXT, City TEXT, PostalCode TEXT, Country TEXT)''')

#Insert values
def InsertCustomers():
    name = raw_input("Customer Name: ")
    contactName = raw_input("Contack Name: ")
    address = raw_input("Address Name: ")
    city =raw_input("City : ")
    post = raw_input("Postal Code :")
    country = raw_input("Country :")        
    cur.execute('''INSERT INTO Customers(CustomerName, ContactName, Address, City, PostalCode, Country)
    VALUES(?,?,?,?,?,?)''',(name, contactName, address, city, post, country))
    con.commit()
    
    
def tampilkan():
        for i in cur:
                print "\n"
                for j in i:
                    print j 
                    
def ShowQuery(query):
    cur.execute(query)
    tampilkan()
        
def menu():
    pilihan=0
    while pilihan !="5" :
        print "1. Add new customer"
        print "2. Show All"
        print "5. Exit"  
        pilihan = raw_input("Choose the number :")     
        if pilihan =="1":
            InsertCustomers()
        if pilihan =="2":
            query = "SELECT * FROM Customers"
            ShowQuery(query)
        
        
#CreateTable()
#print "Pembuatan tabel berhasil"

menu()


