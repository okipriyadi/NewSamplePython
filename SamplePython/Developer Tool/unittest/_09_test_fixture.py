"""
Fixtures are outside resources needed by a test. For example, tests for one class may all
need an instance of another class that provides configuration settings or another shared
resource. Other test fixtures include database connections and temporary files (many
people would argue that using external resources makes such tests not "unit" tests, but
they are still tests and still useful). TestCase includes a special hook to configure and
clean up any fixtures needed by tests. To configure the fixtures, override setUp() . To
clean up, override tearDown() .
"""

import unittest
class FixturesTest(unittest.TestCase):
    def setUp(self):
        print 'In setUp()'
        self.fixture = range(1, 10)

    def tearDown(self):
        print 'In tearDown()'
        del self.fixture
    
    def test(self):
        print 'In test()'
        self.failUnlessEqual(self.fixture, range(1, 10))

if __name__ == '__main__':
    unittest.main()