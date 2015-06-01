"""
In addition to strict equality, it is possible to test for near equality of floating-point
numbers using failIfAlmostEqual() and failUnlessAlmostEqual() .

The arguments are the values to be compared and the number of decimal places to
use for the test.
"""
import unittest

class AlmostEqualTest(unittest.TestCase):
    def testEqual(self):
        self.failUnlessEqual(1.1, 3.3-2.2)

    def testAlmostEqual(self):
        self.failUnlessAlmostEqual(1.1, 3.3-2.2, places=1)

    def testNotAlmostEqual(self):
        self.failIfAlmostEqual(1.1, 3.3-2.0, places=1)

if __name__ == '__main__':
    unittest.main()
