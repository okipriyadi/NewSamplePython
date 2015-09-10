import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

print "menggunakan class========================="
class Oki():
    nama = "oki priyadi"
    panggilan = "oki"
    lahir = "bandung"
    
saya = Oki
mc.set("ini_key1", saya)
value = mc.get("ini_key1")
print "value 1", value.nama
print "value 2", value.panggilan
print "value 3", value.lahir

print "menggunakan dict========================="
ini_dict = {"nami":"oki priyadi", "jenengan":"oki","kawit":"bdg"}
mc.set("ini_key2", ini_dict)
value = mc.get("ini_key2")
print "value 1", value["nami"]
print "value 2", value["jenengan"]
print "value 3", value["kawit"]

