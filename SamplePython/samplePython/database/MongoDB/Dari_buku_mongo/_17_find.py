# A user document demonstrating one-to-many relationships using embedding
         
          
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
    user_doc = {
                "username":"foouser",
                "emails":[
                            {
                            "email":"foouser1@example.com",
                            "primary":True
                            },
                            {
                             "email":"foouser2@example2.com",
                             "primary":False
                            },
                            {
                            "email":"foouser3@example3.com",
                            "primary":False
                            }
                          ]
                }
    # Insert the user document
    dbh.users.insert(user_doc, safe=True)
    # Retrieve the just-inserted document via one of its many email addresses
    user_doc_result = dbh.users.find_one({"emails.email":"foouser1@example.com"})
    # Assert that the original user document and the query result are the same
    
    print user_doc_result
    
if __name__ == "__main__":
    main()
    
