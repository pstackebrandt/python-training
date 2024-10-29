# Time format converter
# Task by https://hyperskill.org/learn/step/47922
# Code by Peter Stackebrandt

"""
We've stored a time value in the 24-hour format in a variable named hour.
Your task is to convert this value to a 12-hour format and print the result.
Note that you should only print the hour as an integer. Do not include AM or PM in your output.

Example:
If hour = 14, the output should be 2.
If hour = 0, the output should be 12.
"""

"""
 further examples
 20 % 12 = 8
 7  % 12 = 7
 1  % 12 = 1
 12 % 12 = 0
"""

def hour_to_hour_12_system_verbose(hour_mix):
    hour12 = hour_mix % 12
    if hour12 == 0:
        hour12 = 12
    return hour12

def hour_to_hour_12_system(hour_mix):
    hour12 = hour_mix % 12
    return 12 if hour12 == 0 else hour12

for hour in [1, 7, 20, 12, 24]:
    print(f"Original: {hour:>2}, 12 hour system: {hour_to_hour_12_system_verbose(hour):>2}")
    print(f"Original: {hour:>2}, 12 hour system: {hour_to_hour_12_system(hour):>2}")

