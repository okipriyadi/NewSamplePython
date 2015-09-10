"""
kesimpuan sementara saya, memcache digunakan untuk menyimpan sebuah value di memori cache 
sehingga program lain bisa mengambil value tersebut dengan cara mencari key yang telah ditetapkan

coba lihat value di file ini bisa didapatkan oleh file _02_test.py

It's fairly simple. You write values using keys and expiry times. You get values using keys. 
You can expire keys from the system. Most clients follow the same rules. 
You can read the generic instructions and best practices on the memcached homepage.
<http://www.danga.com/memcached>
If you really want to dig into it, I'd look at the source. Here's the header comment:
"""
import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

mc.set("some_key", "Some value")
value = mc.get("some_key")
print "value 1", value

mc.set("another_key", 3)
value = mc.get("another_key")
print "value 2", value

mc.delete("another_key")
value = mc.get("another_key")
print "value 3", value

"""
mc.set("key", "1")   # note that the key used for incr/decr must be a string.
mc.incr("key")
mc.decr("key")
key = derive_key(obj)

obj = mc.get(key)
if not obj:
    obj = backend_api.get(...)
    mc.set(key, obj)

# we now have obj, and future passes through this code
# will use the object from the cache.
"""