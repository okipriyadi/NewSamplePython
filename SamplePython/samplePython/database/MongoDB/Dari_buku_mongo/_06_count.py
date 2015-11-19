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
    
    # Find out how many documents are in users collection, efficiently
    userscount = dbh.users.find().count()
    print "There are %d documents in users collection" % userscount
    
if __name__ == "__main__":
    main()
    
