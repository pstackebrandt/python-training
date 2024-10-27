# sumFrations.py

# Task: Calc sum of function 1/(x*x) while x ranges from 2 to 30
# Additional requirements

# Support x = 0 => Result is 0)


def sumFractions(start = 2, end = 30):
    if(start == 0 and end == 0):
        return 0
    return sum(1/(x*x) for x in range(start, end + 1) if x != 0)

# I introduced main() to suppress automatic run of it's content on run of unit tests.
def main():     
    start = 2
    end = 30
    fractSum = sumFractions(start, end + 1)

    print(f'Sum is {fractSum} for fractions with x from {start} to {end}')

if __name__ == '__main__':
    main()
