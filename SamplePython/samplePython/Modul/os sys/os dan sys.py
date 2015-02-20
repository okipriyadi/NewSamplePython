import os
import sys

print "ini path tanpa modul os" 
print __file__

print "\nini path beserta nama filenya: "
print os.path.realpath(__file__)

print "\nini hanya direktori kerjanya saja tanpa disertai filenya "
c = os.path.dirname(os.path.realpath(__file__))
print c

print "\nmenghasilkan file dan folder apa saja yang ada dalam parametr"
print os.listdir(c)

print "\npenggunaan join"
b = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'Assignment5PM')
print b
print os.listdir(b)

print "\nmenggabungkan path" 
a = sys.path.append(b)
print a

print "\ncek apakah folder yang di tuju variabel b sudah masuk path system"
print sys.path

