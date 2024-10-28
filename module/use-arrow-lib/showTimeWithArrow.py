# Use arrow lib to show utc: showTimeWithArrow.py
# Code by Peter Stackebrandt

# Task by Kofler:Python.-2024, 13.5. W2 p. 243
# Use arrow library to show utc.
# Install the library with pip or pip3

# Additional requirements:
# find the library and documentation
# show current utc
# show current time at your home
# show local time stamp
# show time in local time format
# show time in words, eg. 15 Minutes ago
# use a specific locale

# Tasks:
# Calculate the stepsize


import arrow

def main():
    print("Show current time using arrow library")
    
    # show current utc
    currUtc = arrow.utcnow()
    print(f"  utc: {currUtc.format(arrow.FORMAT_ATOM)}")
    
    # show current time at your home
    currLocal = arrow.now()
    print(f"local time: {currLocal.format(arrow.FORMAT_ATOM)}")
    # show local time stamp
    
    localStamp = currLocal.timestamp()
    print()
    print(f"local timestamp: {localStamp}")
    
    # show time only in local time format
    print()
    print(f"local time with german habit: {currLocal.format('HH.mm [Uhr]')}")

    # show time in words, eg. 15 Minutes ago
    print()
    print(f"As people often say - 15 minutes earlier: {arrow.now().shift(minutes=-15).humanize()}")
    
    # use the german locale
    print()
    print(f"In german: 15 minutes later: {arrow.now().shift(minutes=+15).humanize(locale='de')}")
    
       
if __name__ == "__main__":
    main()

"""
Parts of solution    

$ pip install -U arrow
"""