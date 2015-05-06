flight_keys = ('Airline_ID', 'Aircraft_ID', 'Aircraft_Type', 'Aircraft_Tail_Number')

flight_data = dict(zip(flight_keys, [''] * len(flight_keys)))
print flight_data