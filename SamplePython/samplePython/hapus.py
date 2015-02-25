import urllib
import urllib2
import json
import logging

params = urllib.urlencode({'name':'DDT-SAV'})
print params

api_path = 'http://203.142.20.178:4080/master/api/get/file/fdcu/manifest/json/?name=PA-MDCS'


print 'getFDCUManifest api: '
print api_path
auth_man = urllib2.HTTPPasswordMgrWithDefaultRealm()
auth_man.add_password(None, api_path, 'paadmin', 'paadmin')

auth_handler = urllib2.HTTPBasicAuthHandler(auth_man)
rest_opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(rest_opener)

res = urllib2.urlopen(api_path,timeout=20).read()
print res
print type(res)
#convert response to dictionary format
#tricky, json.loads called twice to make response = dict
fdcumanifest_data = json.loads(res)
print type(fdcumanifest_data)
#logging.info(fdcumanifest_data)