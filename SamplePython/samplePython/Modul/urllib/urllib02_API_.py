import urllib
import urllib2
import json
import logging

params = urllib.urlencode({'name':'MDCS-PA'})
print params

api_path = 'http://202.157.168.117/api/fdcs/fdcu/manifest/?%s' %(params)
print 'getFDCUManifest api: '
print api_path
auth_man = urllib2.HTTPPasswordMgrWithDefaultRealm()
auth_man.add_password(None, api_path, 'fdcu', '!fdc8!!23')

auth_handler = urllib2.HTTPBasicAuthHandler(auth_man)
rest_opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(rest_opener)



res = urllib2.urlopen(api_path,timeout=20).read()
#print res
#print type(res)
#convert response to dictionary format
#tricky, json.loads called twice to make response = dict
print res
fdcumanifest_data2 = json.loads(res)
print type(fdcumanifest_data2)
print fdcumanifest_data2
fdcumanifest_data = json.loads(json.loads(res))

print type(fdcumanifest_data)
print fdcumanifest_data
logging.info(fdcumanifest_data)


