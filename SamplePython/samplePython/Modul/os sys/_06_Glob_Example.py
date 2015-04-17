"""
Purpose Use UNIX shell rules to find filenames matching a pattern.
look for a list of files on the file system with names
matching a pattern. To create a list of filenames that all have a certain extension, prefix,
or any common string in the middle
"""
#Buat folder dan file contoh
import os
if not os.path.exists("dir/subdir"):
    os.makedirs("dir/subdir")
if not os.path.exists("dir/subfold"):
    os.makedirs("dir/subfold")    
for i in ["dir/file.txt", "dir/file1.txt", "dir/file2.txt", "dir/filea.txt"
          ,"dir/fileb.txt", "dir/subdir/subfile.txt", "dir/subdir/subfile2.txt", "dir/subfold/subfile2.txt"]:
    if not os.path.exists(i):
        print i , "= file"
        folderna = os.path.dirname(i)
        if not os.path.exists(folderna):
            os.makedirs(folderna)
        f = open(i, "w")
        f.write(i)
        f.close()

#contoh penggunaan glob 
"""
The pattern matches every path name (file or directory) in the directory "dir"
tanpa memasukan subdirektory
"""
import glob
print "contoh awal ========================================="
for name in glob.glob('dir/*'):
    print name



"""
To list files in a subdirectory, the subdirectory must be included in the pattern.
"""
print "search for subdir ========================================="
print 'Named explicitly:'
for name in glob.glob('dir/subdir/*'):
    print '\t', name
    
print 'Named with wildcard:'
for name in glob.glob('dir/*/*'):
    print '\t', name
    



"""
A question mark ( ? ) is another wildcard character. It matches any single character in
that position in the name.
"""
print "? wild card ========================================="
for name in glob.glob("dir/file?.txt"):
    print name
    
    
"""
Use a character range ( [a-z] ) instead of a question mark to match one of several
characters. This example finds all files with a digit in the name before the extension.
"""
print "character range ========================================="
for name in glob.glob('dir/*[0-9].*'):
    print name