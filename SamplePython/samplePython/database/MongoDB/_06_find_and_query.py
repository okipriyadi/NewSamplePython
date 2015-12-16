"""
You can use the find() method to issue a query to retrieve data from a collection in MongoDB. All queries in MongoDB have the scope of a single collection.

Queries can return all documents in a collection or only the documents that match a specified filter or criteria. You can specify the filter or criteria in a document and pass as a parameter to the find() method.

The find() method returns query results in a cursor, which is an iterable object that yields documents.

Prerequisites

The examples in this section use the log collection in the test database. For instructions on populating the collection with the sample dataset, see Import Example Dataset.

In the mongo shell connected to a running mongod instance, switch to the test database.

use test
Query for All Documents in a Collection

To return all documents in a collection, call the find() method without a criteria document. For example, the following operation queries for all documents in the restaurants collection.

===========================
db.log.find()
===========================

Untuk mengetahui jumlah record di tabel tersebut gunakan

===========================
db.log.count()
===========================

Untuk mengskip 
===========================
db.log.find().skip(12092)
===========================

Limit the Number of Documents to Return
The limit() method limits the number of documents in the result set. The following operation returns at most 5 documents in the bios collection:
===========================
db.log.find().limit( 5 )
===========================


Order Documents in the Result Set
The sort() method orders the documents in the result set. The following operation returns documents in the bios collection sorted in ascending order by the name field:
===========================
db.log.find().sort( { _id: 1 } ) 
===========================
1 untuk ascending
-1 untuk descending


contoh kita akan mencari di kolom message yang mengandung kata PA-003 :       *****(kalau di sql rumusnya seperti ini : select * from users where name like '%m%')
==========================================
db.log.find({"msg" : /.*PA-003.*/})
==========================================




contoh lain :
=============================================================
db.users.insert({name: 'paulo'})
db.users.insert({name: 'patric'})
db.users.insert({name: 'pedro'})

db.users.find({name: /a/})  ###like '%a%'
out: paulo, patric

db.users.find({name: /^pa/}) ###like 'pa%' 
out: paulo, patric

db.users.find({name: /ro$/}) ###like '%ro'
out: pedro
=============================================================
"""






"""
The result set contains all documents in the restaurants collection.

Specify Equality Conditions

The query condition for an equality match on a field has the following form:

{ <field1>: <value1>, <field2>: <value2>, ... }
If the <field> is a top-level field and not a field in an embedded document or an array, you can either enclose the field name in quotes or omit the quotes.

If the <field> is in an embedded document or an array, use dot notation to access the field. With dot notation, you must enclose the dotted name in quotes.

Query by a Top Level Field
The following operation finds documents whose borough field equals "Manhattan".

db.restaurants.find( { "borough": "Manhattan" } )
The result set includes only the matching documents.

Query by a Field in an Embedded Document
To specify a condition on a field within an embedded document, use the dot notation. Dot notation requires quotes around the whole dotted field name. The following operation specifies an equality condition on the zipcode field in the address embedded document.

db.restaurants.find( { "address.zipcode": "10075" } )
The result set includes only the matching documents.

For more information on querying on fields within an embedded document, see Embedded Documents.

Query by a Field in an Array
The grades array contains embedded documents as its elements. To specify a condition on a field in these documents, use the dot notation. Dot notation requires quotes around the whole dotted field name. The following queries for documents whose grades array contains an embedded document with a field grade equal to "B".

db.restaurants.find( { "grades.grade": "B" } )
The result set includes only the matching documents.

For more information on querying on arrays, such as specifying multiple conditions on array elements, see Arrays and $elemMatch.

Specify Conditions with Operators

MongoDB provides operators to specify query conditions, such as comparison operators. Although there are some exceptions, such as the $or and $and conditional operators, query conditions using operators generally have the following form:

{ <field1>: { <operator1>: <value1> } }
For a complete list of the operators, see query operators.

Greater Than Operator ($gt)
Query for documents whose grades array contains an embedded document with a field score greater than 30.

db.restaurants.find( { "grades.score": { $gt: 30 } } )
The result set includes only the matching documents.

Less Than Operator ($lt)
Query for documents whose grades array contains an embedded document with a field score less than 10.

db.restaurants.find( { "grades.score": { $lt: 10 } } )
The result set includes only the matching documents.

Combine Conditions

You can combine multiple query conditions in logical conjunction (AND) and logical disjunctions (OR).

Logical AND
You can specify a logical conjunction (AND) for a list of query conditions by separating the conditions with a comma in the conditions document.

db.restaurants.find( { "cuisine": "Italian", "address.zipcode": "10075" } )
The result set includes only the documents that matched all specified criteria.

Logical OR
You can specify a logical disjunction (OR) for a list of query conditions by using the $or query operator.

db.restaurants.find(
   { $or: [ { "cuisine": "Italian" }, { "address.zipcode": "10075" } ] }
)
The result set includes only the documents that match either conditions.

Sort Query Results

To specify an order for the result set, append the sort() method to the query. Pass to sort() method a document which contains the field(s) to sort by and the corresponding sort type, e.g. 1 for ascending and -1 for descending.

For example, the following operation returns all documents in the restaurants collection, sorted first by the borough field in ascending order, and then, within each borough, by the "address.zipcode" field in ascending order:

db.restaurants.find().sort( { "borough": 1, "address.zipcode": 1 } )
The operation returns the results sorted in the specified order.

Additional Information

In the MongoDB Manual, see find(), Cursors, and sort().

In the MongoDB Manual, see also Query Documents tutorial, Projection tutorial, Query and Projection Operators reference, and Cursor Methods.

"""