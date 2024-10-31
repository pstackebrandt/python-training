# miles-to-km-converter.py
# Function to convert miles to kilometers 
"""
Create a function that converts miles to kilometers. The function
should take a single parameter for the distance in miles and return
the equivalent distance in kilometers.
Use the formula: 1 mile = 1.60934 kilometers. Round the result to
two decimal places. Your program should read a single float value
as input (miles) and print the converted distance in kilometers.

from https://hyperskill.org/learn/step/50304
1 mile = 1.60934 kilometers
"""
MILES_TO_KILOMETERS_FACTOR = 1.60934

# Expects float and returns float.
def miles_to_kilometers(miles_f):
    # Your code here
    return round(miles_f * MILES_TO_KILOMETERS_FACTOR, 2)

# Main program
if __name__ == "__main__":
    miles = float(input())
    result = miles_to_kilometers(miles)
    print(f"{result:.2f}")