
#perintah: ubah nilai origin menjadi >4 character atau lebih 

origin = "assasdasdasdasd"
origin = origin[0:4]
print origin
print len(origin)

origin = "as"
origin = origin.rjust(4)
print origin
print len(origin)

origin = "as"
origin = origin.ljust(4)
print origin
print len(origin)
