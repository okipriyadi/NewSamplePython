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
    
    # Return at most 5 users sorted by score in descending order
    # This may be used as a "top 5 users highscore table"
    # Note that a limit of 0 is equivalent to no limit.
    users = dbh.users.find().sort("score", DESCENDING).limit(5)
    for user in users:
        print user.get("username"), user.get("score", 0)
        
if __name__ == "__main__":
    main()
    
