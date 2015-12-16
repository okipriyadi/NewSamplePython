"""
Dalam tugas adiministrasi sistem yang menggunakan Os Linux, kita sering melakukannya 
dengan cara manual (remote menggunakan ssh), tugas administrasi seperti deployment, 
reload services, membuat user baru, memberikan akses user baru, 
tidak terlalu menyulitkan ketika sistem yang diatur hanya sedikit (1 atau 2 host Linux), 
tetapi bagaimana ketika kita harus mengatur sistem yang besar, 
puluhan hingga ratusan server Linux dan pekerjaan administrasi yang berulang? 
tentunya akan menjadi pekerjaan yang tidak mudah. 

Apa itu Fabric?


Fabric adalah Library pada Python yang digunakan untuk berinteraksi terhadap sistem Linux 
menggunakan SSH, yang memudahkan kita melakukan tugas administrasi secara luas, 
berulang, dapat menggunakan orientasi object, mulai dari deployment sampai maintenance 
sistem Linux.

APPLICATION DEPLOYMENT
Deploying an application (regardless of it being a web site, an API, or a server) usually 
means setting up a system from scratch (or from a snapshot taken in time), 
preparing it by updating everything, downloading dependencies, setting up the file structure 
and permissions, followed by finally uploading your codebase - or downloading it using a 
SCM such as Git.



More specifically, Fabric is:

1. A tool that lets you execute arbitrary Python functions via the command line;
2. A library of subroutines (built on top of a lower-level library) to make executing shell commands over SSH easy and Pythonic.


Defnisi tugas administrasi dalam Fabric ditulis dalam sebuah script python, dalam satu folder umumnya
diberi nama fabfile.py dan python script tersebut dapat dieksekusi dengan library Fabric 
yang diinstall secara global dalam Os, cukup dengan menjalankan perintah didalam sebuah 
folder yang memiliki file fabfile.py tersebut:
==========================================
$fab -l
==========================================

Dengan opsi -l tersebut maka akan ditampilkan daftar dari seluruh definisi pekerjaaan 
yang tertulis dalam script python tersebut. 
Bagaimana cara memasang Fabric?

Pada os berbasis Ubuntu yang telah memiliki Python, kita bisa melakukan instalasi 
Fabric dengan menggunakan aptitude
==========================================
$sudo aptitude install fabric
==========================================

Selain itu, Fabric juga dapat diinstall menggunakan Python Package Manager PIP, 
cara ini dapat dijalankan diberbagai os Linux maupun OSX selama pip telah berfungsi dengan benar.
==========================================
$pip install fabric
==========================================


INGAT NAMA FILENYA harus fabfile.py jika bukan makan harus menambahkan perintah -f diikuti nama file
"""