
# Leap year

## Task

Create a simple leap year (Schaltjahr) test.

Task by Kofler:Python.-2024, 9.7. W1 p. 135, 151

## Rules

### Base rules

- Years divisible by 400 without a remainder are indeed leap years.
- Years divisible by 100 without a remainder are not leap years.
- Years divisible by 4 without a remainder are usually leap years.

### Extended Rules

Show days of month! Use this template!
year = 2024
month = 2 # 1 - January, ... 
...
print('der %d. Monat im Jahr %d hat %d Tage.' % (month, year, days))

### My rules
- We check only years with 4 digits.

### Examples

ChatGPT 4o w. Canvas Beta: Here are three years that match the conditions:

1600: Condition 1 - Divisible by 400 (True)
1604: Condition 3 - Divisible by 4, but not by 100 (True)
1608: Condition 3 - Divisible by 4, but not by 100 (True)
The year 1600 meets the condition of being divisible by 400 and is therefore a leap year. The years 1604 and 1608 are divisible by 4, but not by 100, and are also leap years. A year that is only divisible by 100 (but not by 400) would be, for example, 1700, which is not a leap year.

