# test_loopWithCalculatedSteps.py
# Code by Peter Stackebrandt

# Unit tests for loopWithCalculatedSteps.py

from fractions import Fraction
import unittest
import math

from loopWithCalculatedSteps import calcStepSize

class TestLoopWithCalculatedSteps(unittest.TestCase):
    def test_calc_with_start_and_end_but_no_additional_rounds__starting_with_zero(self):
        self.assertEqual(calcStepSize(0, 10, 2), 10)

    def test_calc_with_1_additional_round_starting_with_zero(self):
        self.assertEqual(calcStepSize(0, 10, 3), 5)

    def test_calc_with_1additional_round(self):
        self.assertEqual(calcStepSize(15, 25, 3), 5)

    def test_calc_with_2additional_rounds(self):
        self.assertEqual(calcStepSize(15, 25, 4), Fraction(10,3))

    def test_calc_with_2additional_rounds(self):
        actual = calcStepSize(125, 160, 11)
        self.assertAlmostEqual(actual, 3.5, places=4)

# Der Test-Runner, der die Tests ausführt 
if __name__ == '__main__':
    unittest.main()
