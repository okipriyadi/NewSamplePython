"""
collection bisa dianalogikan dengan tabel
"""
""" An example of how to insert a document """
import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def main():
    try:
        conn = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    
    dbh = conn["apapun"]
    assert dbh.connection == conn
    user_doc = {"username" : "janedoe",
                "firstname" : "Jane",
                "surname" : "Doe",
                "dateofbirth" : datetime(1974, 4, 12),
                "email" : "janedoe74@example.com",
                "score" : 0
                }
    #Jika collection(table) belum ada maka mongo otomatis membuatnya
    #direkomendasikan menggunakan safe=True sehingga insert ke tabel menggunakan metode synchronus, bukan asynchronus sehingga data lebih yakin tersimpan secara menyeluruh
    dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
    
    
if __name__ == "__main__":
    main()
    
"""
satu hal lagi yang perlu diperhatikan, mongodb menggunakan _id sebagai primary key jika kita
tidak menset _id pada perintah insert kita maka mongo secara otomatis membuatkan id untuk kita
"""