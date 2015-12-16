from model import Certificate, ThirdParty, ThirdPartyNode, create_tables
from datetime import datetime

print "==============", datetime.utcnow()


try: 
    Certificate.insert(
                       ts_created = datetime.utcnow(),
                       commonname = 'BBB',
                       digest = 'bbb',
                       not_before = datetime.utcnow(), 
                       not_after = datetime.utcnow(),
                       ).execute()
except:
    print "sudah ada sebelumnya" 
            
try:       
    ThirdParty.insert(
                      certificate = 2,
                      cipherkey = 'aa',
                      initvector = 'b',
    ).execute()
except:
    print "sudah ada sebelumnya" 

try:
    ThirdPartyNode.insert(
                          address = 'localhost',
                          group = 14                
                          ).execute()
except:
    print "sudah ada sebelumnya" 

hasil = Certificate.select(Certificate.not_before, Certificate.not_after,  Certificate.digest, 
                   Certificate.commonname, 
                   ThirdParty.id.alias('thirdparty_id'),  ThirdParty.active, 
                   ThirdParty.sbd_retry_delay.alias('retry_delay'), 
                   ThirdParty.sbd_retry_times.alias('retry_times'), 
                   ThirdParty.sbd_timeout.alias('timeout'),  ThirdParty.quota,
                   ThirdPartyNode.id.alias('tp_node_id')
                   ).join(ThirdParty).join(ThirdPartyNode)
print hasil
print "============"
for i in hasil :
    print i.not_before, i.not_after, i.digest, i.commonname, i.id, i.active, "dll" 
print "====================="

hasil = Certificate.select(Certificate.not_before, Certificate.not_after,  Certificate.digest, 
                   Certificate.commonname, 
                   ThirdParty.id.alias('thirdparty_id'),  ThirdParty.active, 
                   ThirdParty.sbd_retry_delay.alias('retry_delay'), 
                   ThirdParty.sbd_retry_times.alias('retry_times'), 
                   ThirdParty.sbd_timeout.alias('timeout'),  ThirdParty.quota,
                   ThirdPartyNode.id.alias('tp_node_id')
                   ).join(ThirdParty).join(ThirdPartyNode).dicts().first()
print hasil
