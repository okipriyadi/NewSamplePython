parameter_flight_event_mapping = {'WeightOnWheels'     : 'WOW',
                                  'PilotAnnouncement'  : 'PA',
                                'Decompression'      : 'DECOMPRESSION'}

parameter_discrete_mapping      ={'WoW'                : 'WOW',
                                      'DIS_IN_DECOMP_ON'   : 'DECOMPRESSION',
                                      'DIS_IN_PA_ON'       : 'PA'}
timestamp = '0000'
parameter = 'WoW'

if int(timestamp) == 0 and parameter not in parameter_flight_event_mapping.keys() and parameter not in parameter_discrete_mapping.keys():
    print 'yes'
else:
    print 'no'