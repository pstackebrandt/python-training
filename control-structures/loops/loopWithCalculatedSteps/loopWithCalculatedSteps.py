# Loop over a range using a calculated stepsize: loopWithCalculatedSteps.py
# Code by Peter Stackebrandt

"""
# Formulate a loop to iterate through the value range between 125 and 160 in 11 steps.
# The program should output all 11 numbers, starting with 125.0 and ending with 160.0.
"""
# Task by Kofler:Python.-2024, 9.7. W7 p. 152

# Additional requirements:
# Print the numbers with one decimal place.
# Parameter 'rounds' must not be smaller than 2 (start and end point).

# Tasks:
# Calculate the stepsize

from fractions import Fraction

currentValue, stepSize = 0, 0
MIN_VALUE, MAX_VALUE = 125, 160
ROUNDS, MIN_ROUNDS = 11, 2

# Calculates the size of steps which are required to bridge the range between a startvalue and an endvalue.
# Returns Fraction
def calcStepSize(min_val, max_val, expected_rounds = MIN_ROUNDS):
    if expected_rounds < MIN_ROUNDS:
        raise ValueError(f"The parameter is too small: {expected_rounds}. It must be at least {MIN_ROUNDS}.")
        
    val_range = max_val - min_val
    steps_between_borders = expected_rounds - 1 #Start value and end value are outer borders. Between each pair of borders/rounds
    # we have only 1 step (range). So we will have 1 step (range) fewer than borders/rounds. 
    
    return Fraction(val_range, steps_between_borders) # Fraction preserves dividend and divisor 
   
def testTheWest():
    print("Test successful")
    return "Test successful"
    
def main():
    stepSize = calcStepSize(MIN_VALUE, MAX_VALUE, ROUNDS)
    for i in range(ROUNDS):
        print(f"Round: {i:>2} Value: {str(i*stepSize):>6},  {MIN_VALUE + float(i*stepSize):<6.1f}")
    
if __name__ == '__main__':
    main()