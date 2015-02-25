from urllib import *

#urlretrieve digunakan untuk mendownload file yang beradda di server ke folder temm di lokal kita
#untuk dilinux kita bisa lihat hasil downloadnya di folder /tmp
#atau bisa juga terdownload ke folder /home/
#kalau melalui eclipse tidak bisa, coba melalui terminal
#urlretrieve("http://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/1122px-Wikipedia-logo-v2.svg.png", '1122px-Wikipedia-logo-v2.svg.png')


#membuka hubungan
page = urlopen("http://203.142.20.178:4080/master/api/get/file/fdcu/manifest/?%s'name':'MDCS-PA")
#membaca
content = page.read()
print content







