def process_some_data():
    pass

try:
    process_some_data()
except (TypeError, ValueError), e:
    print "ERROR: you provide invalid data", e
except ArithmeticError, e:
    print "ERROR: some math error occurred", e
except Exception, e:
    print "ERROR: you provide invalid data", e

"""
The final except takes advantage of the fact that Exception is the root class for
(almost) all exceptions, so if a thrown exception wasn’t caught by one of the earlier han-
dlers, it would be taken care of in that last statement.
"""