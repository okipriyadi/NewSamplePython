
#perintah: ubah nilai origin menjadi >4 character atau lebih 

origin = "assasdasdasdasd"
if len(origin) >=4:
    origin = origin[0:4]

print origin
print len(origin)

origin = "as"
if len(origin) <=4:
    origin = origin.rjust(4)
print origin
print len(origin)