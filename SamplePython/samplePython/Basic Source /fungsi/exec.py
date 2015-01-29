print "exec() adalah fungsi untuk menerjemaakan string menjadi perintah Python"

while 1 :
    r = raw_input("x = ")
    if r == "" :
        break
    exec("x = " +r)
    print x