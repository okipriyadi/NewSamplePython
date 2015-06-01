"""
Python's unittest module, sometimes called PyUnit, is based on the XUnit frame-
work design by Kent Beck and Erich Gamma. The same pattern is repeated in many
other languages, including C, Perl, Java, and Smalltalk. The framework implemented
by unittest supports fixtures, test suites, and a test runner to enable automated testing.

Tests, as defined by unittest , have two parts: code to manage test dependencies
(called "fixtures") and the test itself. Individual tests are created by subclassing Test-
Case and overriding or adding appropriate methods. For example,
"""

import unittest

class SimplisticTest(unittest.TestCase):
    def test(self):
        self.failUnless(True)#coba ganti true dengan false dan perhatikan beda hasilnya

if __name__ == '__main__':
    unittest.main()

