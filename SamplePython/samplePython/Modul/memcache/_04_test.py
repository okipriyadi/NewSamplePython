#coba lihat di _01_using value yang diset di file tersebut bisa di ambil di file ini selama memory cachenya masih menyimpan data

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)


value = mc.get("ini_key1")
#tak muncul karena classnya bersifat lokal
print "value 1", value


value = mc.get("ini_key2")
print "value 1", value
print "value dari proram lain : ", value['nami']
print "value dari proram lain : ", value['jenengan']
print "value dari proram lain : ", value['kawit']