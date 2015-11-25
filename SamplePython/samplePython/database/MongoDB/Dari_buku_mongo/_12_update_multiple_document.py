"""
At the time of writing, the PyMongo driver, even if you specify a docu-
ment spec to the update method which matches multiple documents in
a collection, only applies the update to the first document matched.
In other words, even if you believe your update document spec matches every single
document in the collection, your update will only write to one of those documents.

For example, let us imagine we wish to set a flag on every document in our users col-
lection which has a score of 0:
even if every document in your collection has a score of 0,
only the first matched document will have its "flagged" property set to True.

dbh.users.update({"score":0},{"$set":{"flagged":True}}, safe=True)

In order to have your update query write multiple documents, you must
pass the "multi=True" parameter to the update method.

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


    # once we supply the "multi=True" parameter, all matched documents will be updated
    dbh.users.update({"score":0},{"$set":{"email":'jane77@jedi.com'}}, multi=True, safe=True)
    print "==================================================================="
    users = dbh.users.find({"firstname":"Jane"}).sort("email", ASCENDING)
    for user in users:
        print user
        
if __name__ == "__main__":
    main()
    