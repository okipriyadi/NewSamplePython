import os
for root,subdirs,files in os.walk("/home/kyi/Dropbox/MDCS"):
    print "root: ",root
    print "subdir: ",subdirs
    print "files: ",files
    print "\n"
    
    files = [f for f in files if not f[0] == '.']
    print "files: ", files
    for fl in files:
        print "fl : ", fl
        