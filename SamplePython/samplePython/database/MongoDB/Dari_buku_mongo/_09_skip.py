"""
When used with limit() this enables
result pagination which is frequently used by clients when allowing end-users to browse
very large result sets. skip() is analogous to the SQL OFFSET statement
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
    
    # Return at most 20 users sorted by name,
    # skipping the first 20 results in the set
    users = dbh.users.find().sort("username", ASCENDING).limit(5).skip(5)
    for user in users:
        print user
if __name__ == "__main__":
    main()
    
