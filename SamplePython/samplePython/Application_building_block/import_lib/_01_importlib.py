"""
penggunaan :
===========================================
importlib.import_module(name, package=None)
===========================================
The name argument specifies what module to import in absolute or relative terms 
(e.g. either pkg.mod or ..mod). If the name is specified in relative terms, 
then the package argument must be specified to the package which is to act as the anchor 
for resolving the package name (e.g. import_module('..mod', 'pkg.subpkg') 
will import pkg.mod). The specified module will be inserted into sys.modules and returned.

Argumen nama menentukan modul apa yang akan diimpor baik secara absolut atau relatif 
(misalnya baik pkg.mod atau ..mod). Jika nama yang ditentukan secara relatif, 
maka argumen package harus ditentukan untuk paket yang bertindak sebagai jangkar 
untuk menyelesaikan nama paket (misalnya import_module ('..mod', 'pkg.subpkg') 
akan mengimpor pkg.mod). Modul yang ditentukan akan dimasukkan ke sys.modules dan akan direturn.
"""
import importlib

mod = importlib.import_module("cilukba")
print mod

app = mod.__getattribute__("ini_pariable")
print app