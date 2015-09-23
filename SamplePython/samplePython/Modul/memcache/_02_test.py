#coba lihat di _01_using value yang diset di file tersebut bisa di ambil di file ini selama memory cachenya masih menyimpan data

import memcache
mc = memcache.Client(['127.0.0.1:11211'], debug=0)

value = mc.get("apps.sbd_api.restart")
print "value dari proram lain : ", value

