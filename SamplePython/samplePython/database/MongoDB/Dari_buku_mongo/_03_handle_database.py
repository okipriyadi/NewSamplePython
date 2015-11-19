""" An example of how to get a Python handle to a MongoDB database """
import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure
def main():
    """ Connect to MongoDB """
    try:
        conn = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    # Get a Database handle to a database named "mydb"
    # jika databse belum ada mongo akan otomatis membuatnya
    dbh = conn["mydb"]
    
        
    #hanya untuk ngecek, sebenarnya tidak diperlukan
    assert dbh.connection == conn
    print "Successfully set up a database handle"

if __name__ == "__main__":
    main()