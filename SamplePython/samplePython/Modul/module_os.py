import os

print "\menghasilkan alamat direktori kerja saat ini"
print os.getcwd()

print "\nmenghasilkan file dan folder apa saja yang ada dalam parametr"
print os.listdir(os.getcwd())

print "\nmembuat direktori baru"
os.mkdir("folderBaru")

print "\nmengubahnama direktori baru"
os.rename("folderBaru", "newFolder")

print "\nmenghapus direktori yang ada"
os.rmdir("newFolder")