"""
Operator         Meaning                 Example                             SQL Equivalent
$gt             Greater Than             “score”:{"$gt”:0}                         >
$lt             Less Than                “score”:{"$lt”:0}                         <
$gte            Greater Than or Equal    “score”:{"$gte”:0}                        >=
$lte            Less Than or Equal       “score”:{"$lte”:0}                        <=
$all            Array Must Contain All   “skills”:{"$all”:["mongodb”,"python"]}   N/A
$exists         Property Must Exist      “email”:{"$exists”:True}                 N/A
$mod            Modulo X Equals Y        “seconds”:{"$mod”:[60,0]}                MOD()
$ne             Not Equals               “seconds”:{"$ne”:60}                     !=
$in             In                       “skills”:{"$in”:["c”,"c++"]}             IN
$nin            Not In                   “skills”:{"$nin”:["php”,"ruby”,"perl"]} NOT IN
$nor            Nor                      “$nor”:[{"language”:"english"},
                                         {"country”:"usa"}]                       N/A
$or             Or                       “$or”:[{"language”:"english"},
                                         {"country”:"usa"}]                       OR
$size          Array Must Be Of Size      “skills”:{"$size”:3}                     N/A
"""