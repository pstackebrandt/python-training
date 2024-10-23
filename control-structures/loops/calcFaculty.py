# Calculate faculty: calcFaculty.py
# Code by Peter Stackebrandt

# Calculate faculty from 1 to 20.
# Task by Kofler:Python.-2024, 9.7. W2 p. 151
# https://de.wikipedia/wiki/Schaltjahr

# Additional requirements:
# Develop different solutions using loops.

# Tasks:

def calFacBySimpleLoop(start, end):
    y = start
    for x in range(start + 1, end + 1):
        y *=x
    return y

start = 1
end = 20
facBySimpleLoop = calFacBySimpleLoop(start, end)

print(f'Faculty from {start} to {end}: {facBySimpleLoop} (Simple loop)')
    
start = 1
end = 3
facBySimpleLoop = calFacBySimpleLoop(start, end)

print(f'Faculty from {start} to {end}: {facBySimpleLoop} (Simple loop)')