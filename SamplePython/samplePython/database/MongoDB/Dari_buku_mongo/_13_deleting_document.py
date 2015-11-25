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


    # Delete all documents in user collection with score 0
    dbh.users.remove({"score":0}, safe=True)
    
    print "==================================================================="
    users = dbh.users.find({"firstname":"Jane"}).sort("email", ASCENDING)
    for user in users:
        print user
        
if __name__ == "__main__":
    main()
    