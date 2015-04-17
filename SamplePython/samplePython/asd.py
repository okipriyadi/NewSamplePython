import os

for root, folder, files in os.walk("/tmp/ddt/globalrepo"):
    print "root",root
    print "folder", folder
    print "files", files
    for fl in files:
        os.remove(os.path.join(root,fl))
        
        