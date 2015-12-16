"""
dari command promt
1. masuk ke superuser (default user biasanya postgres tanpa password)
    sudo -u <user> <password-kalau-ada>
    eg: sudo -u postgres psql
2. create database
    create DATABASE <nama-database>;
3. cek apakah database sudah ada dalam list database
    \l
"""






"""
untuk membuat lebih spesifik databasenya akan di assign ke user mana maka gunakan
1. gak perlu masuk ke superuser cukup di user saat ini
   
2. create database
    createdb -h localhost -p 5432-U postgress testdb
3. cek apakah database sudah ada dalam list database
    psql -l


ATAU BISA JUGA
'sudo -u postgres createdb -U postgres -O igg igg_db'

Option Description
-D     tablespace Specifies the default tablespace for the database.
-e     Echo the commands that createdb generates and sends to the server.
-E     encoding Specifies the character encoding scheme to be used in this database.
-l     locale Specifies the locale to be used in this database.
-T     template Specifies the template database from which to build this database.
--help Show help about dropdb command line arguments, and exit.
-h     host Specifies the host name of the machine on which the server is running.
-p     port Specifies the TCP port or the local Unix domain socket file extension on which the
        server is listening for connections.
-U     username User name to connect as.
-w     Never issue a password prompt.
-W     Force createdb to prompt for a password before connecting to a database.
"""