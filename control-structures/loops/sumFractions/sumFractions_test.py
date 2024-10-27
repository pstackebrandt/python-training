# sumFrations_test.py
# unittest for sumFrations.py

import unittest
from sumFractions import sumFractions

class TestSumFractions(unittest.TestCase):
    
    def test_testing(self):
        #print("test_testing() executed")
        assert True, True
            
    def test_get_sum_for_x_as_2(self):
        #print("test_get_sum_for_x_as_2() executed")
        self.assertAlmostEqual(sumFractions(2, 2), 1/4, places = 4)
        
    def test_get_0_for_x_as_0(self):
        self.assertEqual(sumFractions(0,0), 0)
        
    def test_get_sum_for_x_as_0_to_2(self):
        self.assertAlmostEqual(sumFractions(0, 2), 5/4, places = 4)
    
if __name__ == '__main__':
    unittest.main()