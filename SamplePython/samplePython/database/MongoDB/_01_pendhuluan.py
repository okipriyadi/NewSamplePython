from pymongo import Connection, ASCENDING

#default mongo db berjalan di localhost(127.0.0.1) pada port 27017
conn = Connection('localhost', 27017)

#db = conn["databasesaya"]
db = conn["mongo"]



#melihat jumlah baris
total_data = db.log.count()
print total_data
num_skip   = (total_data - 10) if (total_data > 10) else 0
print num_skip
cursor     = db.log.find(skip = num_skip, tailable = True).sort('$natural', ASCENDING)
print cursor
while True:
    record = cursor.next()
    print record['msg']