"""
Most tests assert the truth of some condition. There are a few different ways to write
truth-checking tests, depending on the perspective of the test author and the desired
outcome of the code being tested

If the code produces a value that can be evaluated as true, the methods
failUnless() and assertTrue() should be used. If the code produces a false value,
the methods failIf() and assertFalse() make more sense.
"""

import unittest
class TruthTest(unittest.TestCase):
    def testFailUnless(self):
        self.failUnless(True)
        
    def testAssertTrue(self):
        self.assertTrue(True)

    def testFailIf(self):
        self.failIf(False)

    def testAssertFalse(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()