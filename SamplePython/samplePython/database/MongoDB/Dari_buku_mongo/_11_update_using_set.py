"""
At the time of writing, the PyMongo driver, even if you specify a docu-
ment spec to the update method which matches multiple documents in
a collection, only applies the update to the first document matched.

Saat disimpan hanya dokumen pertama saja yang akan diubah walaupun where clause nya match dengan beberapa dokumen
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
    
    
    
    # run the update query, using the $set update modifier.
    # we do not need to know the current contents of the document
    # with this approach, and so avoid an initial query and
    # potential race condition.
    dbh.users.update({"username":"janedoe"},
                     {"$set":{"email":"janedoe99@example2.com"}}, 
                     safe=True
                    )
    
    #You can also set multiple properties at once using the $set update modifier:
    # update the email address and the score at the same time
    # using $set in a single write.
    dbh.users.update({"username":"janedoe"},
                     {"$set":{"email":"janedoe74@example2.com", "score":1}}, safe=True)
        
if __name__ == "__main__":
    main()
    
