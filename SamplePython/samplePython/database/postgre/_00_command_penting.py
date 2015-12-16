"""
di cmd untuk restart: service postgresql restart

\l                   :Untuk melihat daftar semua database yg ada
\du                  :Untuk melihat daftar semua user yg ada
\dp                  :Untuk melihat daftar privileges dari setiap
                      object database
\d[NAME]             :Untuk melihat keterangan (describe) dari suatu tabel
                      atau object lainnya
\dt                  :Untuk melihat daftar semua tabel
\c [DBNAME]          :Untuk membuat koneksi ke suatu database agar bisa
                      bekerja di database tsb
select version();    :Untuk mengetahui versi PostgreSQL




You have a PostgreSQL account but where do you start? There are several ways of interacting with PostgreSQL:
1. GUIs: you can use a GUI-based tool, such as pgAdmin, to connect to the database, 
   browse the tables and run queries. 
2. command line: PostgreSQL comes with a very powerful command line utility or interactive 
   terminal called psql. This will be covered in a later post.
3. programmatically: one can use a database driver through code such as the Java JDBC driver. 
   This is a more advanced topic that will not be covered.
"""


