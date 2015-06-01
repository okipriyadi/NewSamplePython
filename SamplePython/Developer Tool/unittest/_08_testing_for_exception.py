"""
As previously mentioned, if a test raises an exception other than AssertionError ,
it is treated as an error. This is very useful for uncovering mistakes while modifying 
code that has existing test coverage. There are circumstances, however, in
which the test should verify that some code does produce an exception. One exam-
ple is when an invalid value is given to an attribute of an object. In such cases,
failUnlessRaises() or assertRaises() make the code more clear than trapping
the exception in the test. Compare these two tests.

The results for both are the same, but the second test using failUnlessRaises() is more succinct.
"""

import unittest
    
def raises_error(*args, **kwds):
    raise ValueError('Invalid value: ' + str(args) + str(kwds))


class ExceptionTest(unittest.TestCase):
    def testTrapLocally(self):
        try:
            raises_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see ValueError')

    def testFailUnlessRaises(self):
        self.failUnlessRaises(ValueError, raises_error, 'a', b='c')

if __name__ == '__main__':
    unittest.main()