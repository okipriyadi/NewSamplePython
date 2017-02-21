"""
A record in MongoDB is a document, which is a data structure composed of field and value pairs.
MongoDB documents are similar to JSON objects. The values of fields may include other 
documents,  arrays, and arrays of documents.
"""

"""
{
   "_id" : ObjectId("54c955492b7c8eb21818bd09"),
   "address" : {
      "street" : "2 Avenue",
      "zipcode" : "10075",
      "building" : "1480",
      "coord" : [ -73.9557413, 40.7720266 ],
   },
   "borough" : "Manhattan",
   "cuisine" : "Italian",
   "grades" : [
      {
         "date" : ISODate("2014-10-01T00:00:00Z"),
         "grade" : "A",
         "score" : 11
      },
      {
         "date" : ISODate("2014-01-16T00:00:00Z"),
         "grade" : "B",
         "score" : 17
      }
   ],
   "name" : "Vella",
   "restaurant_id" : "41704620"
}
"""

"""
Collections

MongoDB stores documents in collections. Collections are analogous to tables in relational 
databases. Unlike a table, however, a collection does not require its documents to have 
the same schema.

In MongoDB, documents stored in a collection must have a unique _id field that acts as 
a primary key.
"""