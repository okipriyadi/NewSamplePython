import os

print os.path.dirname(__file__)

print "Menghasilkan path"
print "ini path : ", os.path.dirname(os.path.realpath(__file__))

print "Menghasilkan ukuran file"
print "ini ukurannya : ", os.path.getsize(__file__)

print "\nmenghasilkan alamat direktori kerja saat ini"
print os.getcwd()

print "\nmenghasilkan file dan folder apa saja yang ada dalam parametr"
print os.listdir(os.getcwd())

print "\nmembuat direktori baru"
os.mkdir("folderBaru")
#atau bisa juga menggunakan
#os.makedirs("folderLain")

print "\nmengubahnama direktori baru"
os.rename("folderBaru", "newFolder")

print "\nmenghapus direktori yang ada"
os.rmdir("newFolder")