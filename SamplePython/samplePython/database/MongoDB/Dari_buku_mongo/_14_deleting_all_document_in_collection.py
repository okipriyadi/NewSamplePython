"""
Finally, if you wish to delete all documents in a collection, you can pass None as a
parameter to remove() :
================================================
dbh.users.remove(None, safe=True)
================================================

Clearing a collection with remove() differs from dropping the collection via 
drop_collection() in that the indexes will remain intact.
"""

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


    # Delete all documents in user collection
    dbh.users.remove(None, safe=True)
    
    print "==================================================================="
    users = dbh.users.find({"firstname":"Jane"}).sort("email", ASCENDING)
    for user in users:
        print user
        
if __name__ == "__main__":
    main()
    