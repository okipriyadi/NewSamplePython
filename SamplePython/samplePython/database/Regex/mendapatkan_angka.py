import re 

s = "how much for the maple syrup? $20.99? That's ricidulous77!!!"
print s
#ganti semua simbol dengan spasi
s = re.findall(r'[0-9]+', s)
print ">>",s
