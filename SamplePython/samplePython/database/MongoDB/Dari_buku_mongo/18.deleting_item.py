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
    # Naive method to remove an email address from a user document Cumbersome and has a race condition
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
    # Retrieve the just-inserted document via username
    user_doc_result = dbh.users.find_one({"username":"foouser"})
    print user_doc_result
    # Remove the "foouser2@example2.com" email address sub-document from the embedded list
    del user_doc_result["emails"][1]    
    print user_doc_result
    # Now write the new emails property to the database
    # May cause data to be lost due to the race between read and write
    dbh.users.update({"username":"foouser"},{"$set":{"emails":user_doc_result}},safe=True)
if __name__ == "__main__":
    main()
    
