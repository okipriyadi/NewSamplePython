"""
To make it easier to understand the nature of a test failure, the fail*() and
assert*() methods all accept an argument msg, which can be used to produce a more
detailed error message.
"""

import unittest
class FailureMessageTest(unittest.TestCase):
    def testFail(self):
        self.failIf(True, 'failure message goes here')

if __name__ == '__main__':
    unittest.main()