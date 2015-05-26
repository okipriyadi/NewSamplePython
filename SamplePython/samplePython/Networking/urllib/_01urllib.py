#hars ada koneksi internet

import urllib
simpenfile = urllib.urlopen("http://www.google.com") #urlopen akan mendownload script layaknya seperti vrowser

print simpenfile
print simpenfile.info()#info() = mereturn metadata dari webuah web
print simpenfile.geturl()#geturl() = mereturn url yg default pada urlopen dalam hal ini misal http://www.google.com/en/us/default.aspx


urllib.urlretrieve('http://www.kaskus.us', "D:/files/kaskus_sdot.html") #urlretrieve akan mendownload layaknya browser(minus gambar) dan disimpan di lokasi yang ditentukan