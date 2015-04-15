import hashlib

def sha1sum(ftosum):
    """
    Compute SHA1 sum of a file
    
    @param ftosum: Path of file to compute
    """
    try:
        with open(ftosum, "rb") as fts:
            fhash = hashlib.new("sha1")
            while True:
                data = fts.read(32768)
                if len(data) != 0:
                    fhash.update(data)
                else:
                    break
            return fhash.hexdigest()
    except IOError:
        pass
pass

def validate_sha1sum(sumfile, ftosum):
    """
    Validate SHA1 file to a given sum file
    
    @param sumfile: Path to sum file of ftosum
    @param ftosum: Path of file to verify
    """
    fs = open(sumfile, "rb")
    try:
        sumval = fs.readline().strip()
        return validate_sha1sum_str(sumval, ftosum)
    finally:
        fs.close()
pass

def validate_sha1sum_str(sumval, ftosum):
    """
    Validate SHA1 file to a given sum string
    
    @param sumfile: Sum of ftosum
    @param ftosum: Path of file to verify
    """
    if len(sumval) == 40 and sumval == sha1sum(ftosum):
        return True
    else:
        return False
pass


file_to_sum = "AWP_CAI_0.1.0_3.db"
ftosum = "/globalrepo/"+ file_to_sum 
sum_nya = sha1sum(ftosum)
print sum_nya
writesumfile = "/home/kyi/"+file_to_sum+".sum"
fs = open(writesumfile, "w")    
sumval = fs.writelines(sum_nya)
fs.close()




