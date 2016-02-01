tailnum = "asdasd"
ack = True
payload = 123
try:
    assert isinstance(tailnum, (str, unicode)), 'TailNum'
    assert isinstance(ack, bool), 'Ack'
    assert isinstance(payload, (str, unicode)), 'errornya_di_Payload'
except AssertionError as e:
    err_msg = str(e)
    if err_msg == 'errornya_di_Payload':
       print "'errornya_di_Payload'"
    else : 
        print "assert ==>", e

