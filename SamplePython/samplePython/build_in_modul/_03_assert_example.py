flight_event = {'PA' :0, 'WOW' : 0, 'DECOMPRESSION' : 0}
flight_keys = ('Airline_ID', 'Aircraft_ID', 'Aircraft_Type', 'Aircraft_Tail_Number')
flight_data = dict(zip(flight_keys, [''] * len(flight_keys)))
flight_subscriber = {}
assert isinstance(flight_subscriber, dict)
assert isinstance(flight_data, dict)
assert isinstance(flight_event, dict)
        