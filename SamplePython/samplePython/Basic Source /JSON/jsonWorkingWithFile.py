import json

x = [1,2,['a','b','c',[1,2,3,{'a':'value'}],3]]
len(x)
data = json.dumps(x)
open('out.json', 'a').write(data)

print "perintah untuk membaca========================="
baca = open('out.json', 'r').read()
data_json = json.loads(baca)
print data_json