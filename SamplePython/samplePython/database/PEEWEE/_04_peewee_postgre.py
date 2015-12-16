"""
Perlu di ubah setingan postgre configuration nya
di /etc/postgresql/9.4/main/pg_hba.conf

ubah ['local', 'all', 'all', 'peer']
menjadi ['local', 'all', 'all', 'trust']
"""

from datetime import datetime
from peewee import PostgresqlDatabase, Model, CharField, BooleanField, DateField


#asumsinya bahwa kita sudah mempunyai user iniuser dgn password inipass di postgre kita
db_connection = PostgresqlDatabase("peewee_db", user="iniuser", password="inipass")
db_connection.connect()

class BaseModel(Model):
    class Meta:
        database = db_connection
        
class Persons(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

Persons.create_table(True)
