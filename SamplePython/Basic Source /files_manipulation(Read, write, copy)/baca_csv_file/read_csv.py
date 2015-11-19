from csv import reader
from traceback import format_exc

dummies={}
try:
    with open("stap_dummy.csv", 'rb') as csvfile:
        rows = reader(csvfile)
        for row in rows:
            kolom1, kolom2, group, parameter, value = row
            #print kolom1, kolom2, group, parameter, value
            if group not in dummies:
                dummies[group] = {parameter : [value]}
            else:                
                if parameter not in dummies[group]:
                    dummies[group][parameter] = [value]
                else:
                    dummies[group][parameter].append(value)
except Exception, e:
    print e
    
print dummies
print "end"