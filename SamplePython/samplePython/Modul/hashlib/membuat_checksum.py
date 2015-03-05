import hashlib

#membuat checksum
def buatCheckSum(full_path_filenya):
    cobaBuat = open(full_path_filenya, "rb") 
    fhash = hashlib.new("sha1")
    while True:
        data = cobaBuat.read()
        fhash.update(data)
        cobaBuat.close()
    return fhash.hexdigest()    

#masukan ful pathnya
namafile = "/home/kyi/hapusaja/API.odt"   
namafile2 = "/home/kyi/hapusaja/fol1/API.odt"
namafile3 = "/home/kyi/hapusaja/folbeda/API.odt"
hasil_checksum = buatCheckSum(namafile)
print hasil_checksum
hasil_checksum2 = buatCheckSum(namafile2)
print hasil_checksum2
hasil_checksum3 = buatCheckSum(namafile3)
print hasil_checksum3


#=================Untuk memvalidasi checksum
def validate_sha1sum(sumfile, ftosum):
    fs = open(sumfile, "rb")
    try:
        sumval = fs.readline().strip()
        return validate_sha1sum_str(sumval, ftosum)
    finally:
        fs.close()

def validate_sha1sum_str(sumval, ftosum):
    compsumval = buatCheckSum(ftosum)
    if len(sumval) == 40 and sumval == compsumval:
        return True
    else:
        return False

