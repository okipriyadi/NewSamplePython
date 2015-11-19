"""
The syntax for calling the connect() function and assigning the results to a
variable is as follows:
=====================================================================================
[variable] = MySQLdb.connect([hostname], [username], [password],[database name])
=====================================================================================

atau bisa juga seperti ini
=====================================================================================
[variable] = MySQLdb.connect(host="[hostname]", user="[username]", passwd="[password]", db="[database name]")
=====================================================================================

"""

import MySQLdb

conn = MySQLdb.connect('localhost', 'root', '1234', "nama_database")


"""
multiple connection

mydb1 = MySQLdb.connect(host="localhost", user="skipper", passwd="mysecret",db="fish")
mydb2 = MySQLdb.connect(host="localhost", user="skipper", passwd="mysecret",db="fruit")
cursor1 = mydb1.cursor()
cursor2 = mydb2.cursor()
"""