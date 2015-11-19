"""
misalkan kita punya data:

user_doc = {
"username" : "okipriyadi07",
"firstname" : "oki",
"surname" : "okip",
"dateofbirth" : datetime(1987, 5, 10),
"email" : "okipriyadi07@example.com",
"score" : 0
}
kita akan mengganti emailnya

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
    assert dbh.connection == conn
    user_doc = {
            "username" : "okipriyadi07",
            "firstname" : "oki",
            "surname" : "okip",
            "dateofbirth" : datetime(1987, 5, 10),
            "email" : "okipriyadi07@example.com",
            "score" : 0
            }
    
    dbh.users.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc
    
    # Return at most 5 users sorted by score in descending order
    # This may be used as a "top 5 users highscore table"
    # Note that a limit of 0 is equivalent to no limit.
    import copy
    users = dbh.users.find({"username":"okipriyadi07"})
    new_users= copy.deepcopy(users)
    # modify the copy to change the email address
    for new_user in new_users:
        new_user["email"] = "oki7777@example2.com"
    # run the update query
    # replace the matched document with the contents of new_user_doc
    dbh.users.update({"username":"okipriyadi07"}, new_user, safe=True)
 
        
if __name__ == "__main__":
    main()
    
