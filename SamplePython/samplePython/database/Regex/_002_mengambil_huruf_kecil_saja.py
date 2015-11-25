"""
bukan huruf kecil
Catatan, ini berarti angka, simbol, maupun huruf besar cocok dengan pola ini. 
Karena semuanya bukan huruf kecil.

[^a-z]
"""

import re 

s = "hOw mUch for the maPle syrup? $20.99? That's ricidulous!!!"
print s
#ganti selain huruf kecil dengan spasi
d = re.sub(r'[^a-z]', ' ', s)
print d
#ganti selain huruf besar dengan spasi
e = re.sub(r'[^A-Z]', ' ', s)
print e

