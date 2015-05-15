string_02 = "/data/vps1/ashdkas"
path2 = string_02.split("/")
path3 = string_02.rsplit("/")
print "path2 : ", path2
print "path3 : ", path3
print len(path2)
print type(path2)
print path2[3]

#another example
string_03 = "saya menjadi \n  apa yang saya mau \n udah sih gitu ajah"
print string_03
test_04,test_05,test_02 = string_03.split("\n")

#print test_04
print "test_04", test_04
print "test_05", test_05
print "test_02", test_02

string_01 = "u'81514_The_Adventures_of_Tintin_The_Secret_of_the_Unicorn_UNION_SELECT_2011_BluRay720.mkv"
#memisahkan dengan pisahan "_" sebanyak 2 "_" dimulai dari 
test = string_01.split('_',2)
print "test :", test
test_with_index = string_01.split('_')[1]
print "ambil hasil split index ke 1 =", test_with_index
datagroup = string_01.rsplit('_',2)
print "datagroups", datagroup