"""fileno menghasilkan integer dari file description yang digunakan untuk mengimplementasikan 
request ke I/O operation dari sistem operasi
"""

#Open file
fo = open("test.txt", "wb")
print "Name of the file:", fo.name

fid = fo.fileno()
print "File descriptor: ", fid

#close file
fo.close()