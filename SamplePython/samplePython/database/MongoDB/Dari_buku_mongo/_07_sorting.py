import sys
from datetime import datetime
from pymongo import Connection, ASCENDING, DESCENDING
from pymongo.errors import ConnectionFailure

def main():
    try:
        conn = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    
    dbh = conn["apapun"]
    assert dbh.connection == conn
    user_doc = {"username" : "budilaksono",
                "firstname" : "Jane",
                "surname" : "bulak",
                "dateofbirth" : datetime(1974, 4, 12),
                "email" : "balik000000@example.com",
                "score" : 0
                }
    dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
    
    # Return all user with firstname "jane" sorted
    # in descending order by birthdate (ie youngest first)
    users = dbh.users.find({"firstname":"Jane"}).sort("email", DESCENDING)
    for user in users:
        print user
    
    print "==================================================================="
    users = dbh.users.find({"firstname":"Jane"}).sort("email", ASCENDING)
    for user in users:
        print user
        
if __name__ == "__main__":
    main()
    
