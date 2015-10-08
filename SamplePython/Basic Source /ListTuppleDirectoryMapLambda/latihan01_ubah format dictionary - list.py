fdcumanifest_data = {u'fleets': [{u'aircrafts': [u'TC-TJN', u'TC-TJK', u'TC-TJM', u'TC-TJO'], u'name': u'717', u'groups': [{u'category': u'software', u'name': u'AWP_CAI_0.2.0'}, {u'category': u'hot_sync', u'name': u'ICLOUD DATA'}]}], u'version': 3, u'aircrafts': [u'TC-TJK;CAI;5a62230cde014dd1a85da95616ebee535b41cf38', u'TC-TJM;CAI;92fce041d16461fde08d891f069a6e97651e3a1c', u'TC-TJN;CAI;92fce041d16461fde08d891f069a6e97651e3a1c', u'TC-TJO;CAI;92fce041d16461fde08d891f069a6e97651e3a1c'], u'acrls': [u'AWP_CAI_0.2.0;8fbdd8b6a7bc4f32ec7c3e865c26710d694086e0;AWP_CAI_0.1.0;123456-789-00;1', u'ICLOUD DATA;91675d38f91a9772fbfed31cf86b3e2fbf57a82b;No;No;1'], u'total': 3, u'size': 5629793}
print fdcumanifest_data
#Format fdcumanefest_data
i = 0
#change from key_name = 'name' to key_name='fleet'
for fleet in fdcumanifest_data['fleets'] :
    fdcumanifest_data['fleets'][i][unicode('fleet')] = fdcumanifest_data['fleets'][i].pop('name') 
    i = i + 1

#change format aircrafts
temp_list = []
for aircraft in fdcumanifest_data['aircrafts']:
    tail_number,airline,manifest_aircraft_sha = aircraft.split(";")
    a = {unicode("tail_number"):tail_number,unicode("airline"):airline,unicode("manifest_aircraft_sha"):manifest_aircraft_sha}
    temp_list.append(a)
del(fdcumanifest_data['aircrafts'])
fdcumanifest_data.update({unicode("aircrafts"):temp_list})
 
#change format ACRLs
temp_list = [] 
for acrl in fdcumanifest_data['acrls']:
    category, sha, group, version, group_id = acrl.split(";")
    a = {unicode("category"):category, unicode("sha"):sha, unicode("group"):group, unicode("version"):version, unicode("group_id"):group_id}
    temp_list.append(a)
del(fdcumanifest_data['acrls'])
fdcumanifest_data.update({unicode("acrls"):temp_list})
print fdcumanifest_data


    