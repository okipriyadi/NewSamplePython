import os
for root,subdirs,files in os.walk("/globalrepo"):
    print os.path.join(root, subdirs, files)
    