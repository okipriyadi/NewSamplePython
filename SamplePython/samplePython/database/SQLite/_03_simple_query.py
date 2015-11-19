import os
import sqlite3

conn=sqlite3.connect('sample_database')
cursor = conn.cursor()

cursor.execute(""" select employee.firstname, employee.lastname, department.name
                   from employee, department
                   where employee.dept = department.departmentid
                   order by employee.lastname desc
                """)
for rows in cursor.fetchall():
    a = rows
    print(rows)

print "===============================================================================" 
print a 
print type(a)
b, c, d = a
print b
print c 
print d

print "==============================================================================="
print "Lihat kalau di fetch(ambil) lagi tidak ditampilkan apa-apa karna data sudah diambil, maka harus query (execute) lagi"
for rows in cursor.fetchall():
    print(rows)
print "kosong"

print "==============================================================================="
print "execute lagi"
cursor.execute(""" select employee.firstname, employee.lastname, department.name
                   from employee, department
                   where employee.dept = department.departmentid
                   order by employee.lastname desc
                """)
for rows in cursor.fetchall():
    print(rows)


print "==============================================================================="
cursor.execute(""" select employee.firstname, employee.lastname, department.name
                   from employee, department
                   where employee.dept = department.departmentid
                   order by employee.lastname desc
                """)
for rows in cursor.fetchall():
    for row in rows:
        a = row
        print row
        
print "===============================================================================" 
print a 
print type(a)

cursor.close()