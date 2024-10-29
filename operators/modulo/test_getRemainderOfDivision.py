# test_getRemainderOfDivision.py

import unittest

from getRemainderOfDivision import getRemainderOfDivision as getRemainder

class testGetRemainder(unittest.TestCase):
    def test_remainder_of_5_by_2(self):
        actual = getRemainder(5, 2)
        self.assertEqual(actual[0], 1)
    
    def test_quotient_of_5_by_2(self):
        actual = getRemainder(5, 2)
        self.assertEqual(actual[1], 2)

    def test_remainder_of_4_by_2(self):
        actual = getRemainder(4, 2)
        self.assertEqual(actual[0], 0)
    
    def test_quotient_of_4_by_2(self):
        actual = getRemainder(4, 2)
        self.assertEqual(actual[1], 2)
        

# Call test runner
if __name__ == '__main__':
    unittest.main()