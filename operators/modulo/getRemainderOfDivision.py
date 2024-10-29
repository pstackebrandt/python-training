# Get the remainder of integer division: getRemainderOfDivision.py

# Requirements
# - Show that the algorithm to get the remainder works.
# - We don't need to queck edge cases, eg. behaviour on divisor = 0.

# returns remainder and quotient of integer division in a tupel.
def getRemainderOfDivision(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend - (quotient * divisor)
    return((remainder, quotient))

