"""
1. pertama-tama pastikan modul untuk database yang akan kita gunakan telah tersedia
misal untuk menggunakan mysql diguankan modul  " import MySQLdb " sebagian lain mengharuskan kita mendowload karna modul tersebut tidak disediakan python secara defaut

2. buat koneksi. Program butuh berkomunikasi kepada database yang digunakan. assumsinya database berjalan pada process yang berbeda dengan aplikasi sehingga butuh koneksi agar bisa terhubung.
===========================================================================
conn = dbmodule .connect(dsn=’localhost:MYDB’,user=’tiger’,password=’scott’)
===========================================================================

Parameter         Usage
Dsn               Data source name, from ODBC terminology. This usually includes the name of your database and the server where it ’ s running.
Host              Host, or network system name, on which the database runs.
Database          Name of the database.
User              User name for connecting to the database.
Password          Password for the given user name. 

contoh jika database menggunakan mysql maka
===========================================================================
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","0608810","phone" )
===========================================================================

3. Gunakan cursor sebagai objek yang menjadikan kita bisa bekerja dengan database
Dalam istilah database, cursor diposisikan dilokasi tertentu dalam sebuah tabel atau bahkan tables dalam database, 
seperti cursor yang terdapat di screen ketika kamu mengedit sebuah dokumen, yang lokasinya pada pixel tertentu.

untuk mendapatkan object cursor, kamu harus memanggil cursor method pada object connection yang telah dibuat sebelumnya:
============================
cursor = conn.cursor()
============================
Once you have a cursor, you can perform operations on the database, such as inserting records. 
"""