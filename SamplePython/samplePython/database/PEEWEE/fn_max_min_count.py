from peewee import SqliteDatabase, IntegerField, Model, Check, DateTimeField, CharField, TextField, fn
from datetime import datetime
sqlite_db = SqliteDatabase('contoh.db')

class SQLiteBaseModel(Model):
    class Meta:
        database = sqlite_db

class SBDAPIMessage(SQLiteBaseModel):
    unique_id = IntegerField(unique=True, constraints=[Check('unique_id > 0')])
    msg_id = IntegerField(null=True, constraints=[Check('msg_id >= 0'), Check('msg_id <= 65535')])
    ts_sent = DateTimeField(default=datetime.utcnow)
    ts_sent_ack = DateTimeField(null=True)
    ts_forward = DateTimeField(null=True)
    ts_forward_ack = DateTimeField(null=True)
    status = IntegerField(default=0, choices=((0, 'not-sent'),
                                              (1, 'sent not acknowledged'),
                                              (2, 'sent and acknowledged'),
                                              (3, 'forwarded not acknowledged'),
                                              (4, 'forwarded and acknowledged'),
                                              (5, 'failed')))
    tailnum = CharField()
    ack = IntegerField()
    payload = TextField()
    remarks = TextField(null=True)



SBDAPIMessage.create_table(True)
for i in [2,3,4,5]:
    try: 
        SBDAPIMessage.insert(unique_id=i, status=1, tailnum='PA-001', ack=1, payload="xxyyy").execute()
        print "simpan id =", i
    except:
        print "id sudah ada"
        
semua = SBDAPIMessage.select(SBDAPIMessage.unique_id).where(SBDAPIMessage.unique_id > 0)
last = SBDAPIMessage.select(SBDAPIMessage.unique_id).where(SBDAPIMessage.unique_id > 0).aggregate(fn.Max(SBDAPIMessage.unique_id))
start = SBDAPIMessage.select(SBDAPIMessage.unique_id).where(SBDAPIMessage.unique_id > 0).aggregate(fn.Min(SBDAPIMessage.unique_id))
count = SBDAPIMessage.select(SBDAPIMessage.unique_id).where(SBDAPIMessage.unique_id > 0).aggregate(fn.count(SBDAPIMessage.unique_id))
print "==============================="
print "tampilkan semua id :"
for satu in semua:
    print satu.unique_id
print "==============================="
print "fn.max = ",last
print "fn.min =", start
print "fn.count", count