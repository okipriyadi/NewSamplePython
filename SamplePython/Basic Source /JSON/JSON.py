import json

print "Cara encode json dibandingkan dengan list ==========================================" 
data = [{'a':'A', 'b':(2,4), 'c':3.0}]
print 'DATA' ,data

data_string = json.dumps(data)
print 'JSON :', data_string
print type(data_string)
print "terlihat sebelum dilakukan load, data masih berupa string"

print "Encoding kemudian recording ================================================================"
print 'ENCODE : ', data_string
decode = json.loads(data_string)
print 'Decode : ', decode
print data[0]['b']
print "Original : ", type(data[0]['b'])
print decode[0]['b']
print "Decode : ", type(decode[0]['b'])

print "JSON sorting ================================================================"
unsorted = json.dumps(data)
print unsorted
sort = json.dumps(data, sort_keys=True)
print sort
first =json.dumps(data, sort_keys=True)
print first
print "Unsorted match: ", unsorted ==sort
print "Sorted match: ", first ==sort

print "Output Indent ================================================================"
indent = json.dumps(data, sort_keys=True, indent=2)
print indent

print "Error Key ================================================================"
#The JSON format expects the keys to a dictionary to be strings. If you have other types as keys in your dictionary, trying to encode the object will produce a ValueError. One way to work around that limitation is to skip over non-string keys using the skipkeys argument:
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0, ('d',):'D tuple' } ]

print 'First attempt'
try:
    print json.dumps(data)
except (TypeError, ValueError) as err:
    print 'ERROR:', err

print
print 'Second attempt'
print json.dumps(data, skipkeys=True)
#Rather than raising an exception, the non-string key is simply ignored.

