import re 
pilihan = 0;
while (pilihan!="6"):
    print "================Regex=================="
    print "1. Validasi Email"
    print "2. Filtering"
    print "3. dapatkan no HP"
    pilihan = raw_input("pilih: ")
    if pilihan =="1" :
        print "----------------------------Validasi email---------------------" 
        email = raw_input("masukan email:")
        hasil = re.search('[\w.-]+@[\w.-]+\.\w+', email)
        if hasil :
            print hasil.group(), "adalah email valid"
        else:
            print "bukan alamat email yang valid"  
        
    if pilihan == "2":
        pat = re.compile(r'(FUCK)|(DAMN)', re.IGNORECASE)
        s = "fuck yeah mahasiswa, you really damn"
        print pat.sub('****',s)

        
    if pilihan == "3":
        pat = re.compile('(0|62)[0-9]+')
        text = "uasdukhasjdha 08674364526745"
        text = pat.search(text)
        print text.group()