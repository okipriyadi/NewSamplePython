import sqlite3
con = sqlite3.connect('Toko.db')
# prepare a cursor object using cursor() method
cur = con.cursor()

#Query put Here
cur.execute('SELECT SQLITE_VERSION()')

# Fetch a single row using fetchone() method.
data = cur.fetchone()

#print the data
print "SQLite version: %s" % data

#Create tabel
#cur.execute('''CREATE TABLE Customers(CustomerID INTEGER PRIMARY KEY AUTOINCREMENT, 
#CustomerName TEXT, ContactName TEXT, Address TEXT, City TEXT, PostalCode TEXT, Country TEXT)''')

def insertCustomer():
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
        
def showQuery():
    query = "Select * From Customers ORDER BY CustomerName Desc"
    cur.execute(query)
    tampilkan()


def search():
    searchKey = raw_input("masukan kata kunci")
    query = "SELECT * FROM Customers WHERE CustomerName LIKE '%" + searchKey + "%' OR ContactName LIKE '%"+searchKey+ "%' OR Address LIKE '%"+searchKey+"%' OR City LIKE '%"+searchKey+"%' OR PostalCode LIKE '%"+searchKey+"%' OR Country LIKE '%"+searchKey+"%'"
    cur.execute(query)
    tampilkan()
    
def delete():
    search()
    IdDelete = raw_input("Pilih ID untuk di delete : ")
    query = "DELETE FROM Customers WHERE CustomerID = '"+IdDelete+"'"
    cur.execute(query)
    print "No Id :", IdDelete, "berhasil di delete"
    con.commit()
    
def editKontak():
    search()
    CustomerID = raw_input("Masukan no customer Id yang akan diedit")
    nama = raw_input("masukan nama :")
    query = "UPDATE Customers SET CustomerName='"+ nama +"', City='Hamburg' WHERE CustomerID='"+ CustomerID +"'" 
    cur.execute(query)
    con.commit()
    
def menuCustomer():
    pilihan = "0"
    while pilihan !="9":
        print "===========Menu============"
        print "1. Add new customer"
        print "2. Show All"
        print "3. Cari"
        print "4. Delete"
        print "5. Edit"
        print "9. Exit"  
        pilihan = raw_input("Choose the number :")     
        if pilihan =="1":
            insertCustomer()
        if pilihan =="2":
            showQuery()
        if pilihan =="3":
            search() 
        if pilihan =="4":
            delete()
        if pilihan =="5":
            editKontak()

    
    

def menuUtama():
    pilihan = "0"
    while pilihan !="9":
        print "===========Menu============"
        print "1. Masuk Tabel Customer"
        print "2. Sample Inner join"
        print "3. Left Join"
        print "9. Exit"
        pilihan = raw_input("Choose the number :")     
        if pilihan =="1":  
            menuCustomer()
        if pilihan =="2":
            query = "select orderan.order_id, Customers.CustomerName, orderan.order_date from Orderan JOIN Customers ON orderan.id_person = customers.CustomerID ORDER BY Customers.CustomerName"
            cur.execute(query)
            tampilkan()
        if pilihan =="3":
            query = "select orderan.order_id, Customers.CustomerName, orderan.order_date from Orderan LEFT JOIN Customers ON orderan.id_person = customers.CustomerID ORDER BY Customers.CustomerName"    
            cur.execute(query)
            tampilkan()
        if pilihan =="4":
            query = "select orderan.order_id, Customers.CustomerName, orderan.order_date from Orderan RIGHT OUTER JOIN Customers ON orderan.id_person = customers.CustomerID ORDER BY Customers.CustomerName"    
            cur.execute(query)
            tampilkan()
            
        
    
menuUtama()

