"""
Tests have three possible outcomes
1. OK         : test berhasil
2. Fail       : test tidak berhasil dan menghasilkan Assertionerror
3. ERROR      : test tidak berhasil menghasilkan exception selain dari assertionerror

"""

import unittest

class OutcomesTest(unittest.TestCase):
    def testPass(self):
        return
    
    def testFail(self):
        self.failIf(True)
        
    def testError(self):
        raise RuntimeError('test Error')
    
if __name__ == '__main__':
    unittest.main() 
