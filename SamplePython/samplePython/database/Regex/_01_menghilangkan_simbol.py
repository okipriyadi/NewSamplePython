import re 

s = "how much for the maple syrup? $20.99? That's ricidulous!!!"
print s
#ganti semua simbol dengan spasi
s = s = re.sub(r'[^0-9a-zA-Z]+', ' ', s)
print s
