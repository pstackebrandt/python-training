# Calculate faculty: calcFaculty.py
# Code by Peter Stackebrandt

# Calculate faculty from 1 to 20.
# Task by Kofler:Python.-2024, 9.7. W2 p. 151
# https://de.wikipedia/wiki/Schaltjahr

# Additional requirements:
# Develop different solutions using loops.

# Tasks:

import math
from functools import reduce

def calcFacBySimpleLoop(start, end):
    y = start
    for x in range(start + 1, end + 1):
        y *=x
        
    return y

def calcFacUsingMathProd(start, end):
    return math.prod(x for x in range(start, end + 1))
    
def calcFacUsingGeneratorExpression(start, end):
    factors = [x for x in range(start + 1, end + 1)]
    return reduce(lambda x, y : x * y, factors, 1)

start = 1
end = 20
facBySimpleLoop = calcFacBySimpleLoop(start, end)

print(f'Faculty from {start} to {end}: {facBySimpleLoop} (Simple loop)')
    
start = 1
end = 3
facBySimpleLoop = calcFacBySimpleLoop(start, end)

print(f'Faculty from {start} to {end}: {facBySimpleLoop} (Simple loop)')

start = 1
end = 20
facByMathProd = calcFacUsingMathProd(start, end)

print(f'Faculty from {start} to {end}: {facByMathProd} (using math.prod())')

start = 1
end = 20
facByGenExpr = calcFacUsingGeneratorExpression(start, end)

print(f'Faculty from {start} to {end}: {facByGenExpr} (using generator expression)')