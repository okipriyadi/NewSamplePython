"""
mengembalikan objek proxi yang mendelegasikan ke parent atau sibling class (saudara kandung). 
Hal ini berguna untuk mengakses metode warisan yang telah diganti (overridden) dalam sebuah kelas.

ada dua kasus penggunaan yang khas untuk super. Dalam hirarki kelas dengan pewarisan tunggal, 
super bisa digunakan untuk merujuk ke kelas induk tanpa menyebut secara explisit. 

kegunaan kedua adalah mendukung multiple inheritance dalam dinamyc environtment. kasus ini unik 
yang hanya bisa terjadi di python. ini memungkinkan menerapkan diagram diamond dimana beberapa kelas dasar menerapkan metode yang sama. 
"""