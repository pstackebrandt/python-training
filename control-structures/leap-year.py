# leap-year.py
# Create a simple leap year (Schaltjahr)test.
# 
# Base rules:
# Years divisible by 400 without a remainder are indeed leap years.
# Years divisible by 100 without a remainder are not leap years.
# Years divisible by 4 without a remainder are usually leap years.

# We check only years with 4 digits.
'''
ChatGPT 4o w. Canvas Beta: Here are three years that match the conditions:

1600: Condition 1 - Divisible by 400 (True)
1604: Condition 3 - Divisible by 4, but not by 100 (True)
1608: Condition 3 - Divisible by 4, but not by 100 (True)
The year 1600 meets the condition of being divisible by 400 and is therefore a leap year. The years 1604 and 1608 are divisible by 4, but not by 100, and are also leap years. A year that is only divisible by 100 (but not by 400) would be, for example, 1700, which is not a leap year.

'''

def getYearFromUser():
    print("""Bitte gebe das zu prüfende Jahr ein!
    Nutze bitte 4 Ziffern""")
    
    # ask for year (if not done 3 times already)
    askTimesLeft = 3
    year = None
    while(askTimesLeft > 0 and year == None):
        yearIn = input("Jahr: ")
        askTimesLeft -= 1 
        # check input
        try: 
            year = int(yearIn)
            # check size of year
            if year < 999:
                print(f"Die Jahreszahl {year} ist zu klein.")
                year = None
            elif year > 9999:
                print(f"Die Jahreszahl {year} ist zu groß.")
                year = None
            else:
                print(f"Die Jahreszahl {year} kann verwendet werden.")
        except Exception as e: 
            print(f"""Die Eingabe '{yearIn}' ist leider keine Zahl.
    Versuche es noch einmal!""")
        finally:
            if year == None:
                tries = 'Versuche' if askTimesLeft == 2 else 'Versuch' 
                print(f"Du hast noch {askTimesLeft} {tries}.")
        
    return year

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0: 
        return True

def outputResults(year, isLeapYear):
    # print results
    if isLeap: 
        print(f"Das Jahr {year} ist ein Schaltjahr.")
    else:
        print(f"{year} ist kein Schaltjahr.")

print("Schaltjahrtest")
year = getYearFromUser()
print(f"Das Jahr {year} wird geprüft.")
isLeap = isLeapYear(year)
outputResults(year, isLeap)






    
