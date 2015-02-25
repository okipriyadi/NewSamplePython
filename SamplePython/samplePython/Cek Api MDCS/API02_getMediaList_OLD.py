import urllib2
import json 

api_path= 'http://202.157.168.117/api/fdcs/datagroup/?acrl_name=XAX-JEPPESSEN+AIRPORT+CHARTS_HS_370.db&fleet_name=XAX-PA-FLEET'
auth_man = urllib2.HTTPPasswordMgrWithDefaultRealm()
auth_man.add_password(None, api_path, 'fdcu', '!fdc8!!23')
            
auth_handler = urllib2.HTTPBasicAuthHandler(auth_man)
rest_opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(rest_opener)
            
res = urllib2.urlopen(api_path,timeout=20).read()
#convert response to dictionary format
#tricky, json.loads called twice to make response = dict
print type(res)
print res
media_data = json.loads(json.loads(res))
print "after json load",type(media_data)
print media_data
 