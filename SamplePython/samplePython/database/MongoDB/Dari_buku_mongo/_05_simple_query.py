"""
Sample query document to match all documents in the users collection with firstname
"jane":
===============================================
q = {
    "firstname" : "jane"
    }
===============================================

If we wanted to retrieve all documents with firstname "jane" AND surname "doe", we
would write:
===============================================
q = {
    "firstname" : "jane",
    "surname" : "doe"
    }
===============================================

If we wanted to retrieve all documents with a score value of greater than 0, we would
write:
===============================================
q = {
    "score" : { "$gt" : 0 }
    }
===============================================
"""



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
    dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
    
    #menampilkan satu saja, nilai returnnya berupa dictionary
    #Notice that find_one() will return None if no document is found.
    user_doc = dbh.users.find_one({"username" : "janedoe"})
    if not user_doc:
        print "no document found for username janedoe"
    else :
        print user_doc
    
    print "============================"
    #menampilkan semuanya 
    user_doc = dbh.users.find({"username" : "janedoe"})
    for user in user_doc:
        print user
    
    print "============================"
    #hanya menampilkan kolom email saja
    users = dbh.users.find({"firstname":"Jane"})
    for user in users:
        print user.get("email")
        
    
if __name__ == "__main__":
    main()
    
