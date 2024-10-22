# Leap year: leap-year.py
# Code by Peter Stackebrandt

# Create a simple leap year test(Schaltjahr).
# Task by Kofler:Python.-2024, 9.7. W1 p. 135, 151
# https://de.wikipedia/wiki/Schaltjahr

# Tasks:
# todo Add tests
# todo    for each leap and not leap years
# todo    for days of month (leap, not leap, different month)
# ok: Get month (1-12) from user
#   ok: Check input
#   Monatsname bei Eingabeauswertung anzeigen
# ok: calculate days
# ok: print days

MONTHS_DATA = (
    ('Januar', 'January', 1, 31),
    ('Februar', 'February', 2, 28),
    ('März', 'March', 3, 31),
    ('April', 'April', 4, 30),
    ('Mai', 'May', 5, 31),
    ('Juni', 'June', 6, 30),
    ('Juli', 'July', 7, 31),
    ('August', 'August', 8, 31),
    ('September', 'September', 9, 30),
    ('Oktober', 'October', 10, 31),
    ('November', 'November', 11, 30),
    ('Dezember', 'December', 12, 31)
)

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

def getMonthNumberFromUser():
    print("""Für welchen Monat sollen die Tage berechnet werden?
    Nutze bitte die Zahlen 1 - 12""")
    
    # ask for month (if not done 3 times already)
    askTimesLeft = 3
    monthNumber = None
    while(askTimesLeft > 0 and monthNumber == None):
        monthIn = input("Monat: ")
        askTimesLeft -= 1 
        # check input
        try: 
            monthNumber = int(monthIn)
            # check size of monthNumber
            if monthNumber < 1:
                print(f"Die Monatsnummer {monthNumber} ist zu klein.")
                monthNumber = None
            elif monthNumber > 12:
                print(f"Die Monatsnummer {monthNumber} ist zu groß.")
                monthNumber = None
            else:
                monthName = getMonthName(monthNumber)
                print(f"Die Monatsnummer {monthNumber} vom {monthName} kann verwendet werden.")
        except Exception as e: 
            print(f"""Die Eingabe '{monthIn}' ist leider keine Zahl.
    Versuche es noch einmal!""")
        finally:
            if monthNumber == None:
                tries = 'Versuche' if askTimesLeft == 2 else 'Versuch' 
                print(f"Du hast noch {askTimesLeft} {tries}.")
    return monthNumber

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0: 
        return True

def getDaysOfMonth(monthNumber, isLeapYear):
    if isLeapYear and monthNumber == 2:
       return 27
    else:    
       return MONTHS_DATA[monthNumber-1][3]

def getMonthName(monthNumber):
    return MONTHS_DATA[monthNumber-1][0]

def outputLeapYear(year, isLeapYear):
    # print results
    if isLeap: 
        print(f"Das Jahr {year} ist ein Schaltjahr.")
    else:
        print(f"{year} ist kein Schaltjahr.")

def outputDaysOfMonth(days, monthNumber, year, isLeap):
    print(f"Der {getMonthName(monthNumber)} {year} hat {days} Tage.")

'''
Show days of month! Use this template!
year = 2024
month = 2 # 1 - January, ... 
...
print('der %d. Monat im Jahr %d hat %d Tage.' % (month, year, days))
'''

print("Schaltjahrtest")

year = getYearFromUser()
monthNumber = getMonthNumberFromUser()
print(f"Das Jahr {year} und der Monat {monthNumber} werden geprüft.")

isLeap = isLeapYear(year)
days = getDaysOfMonth(monthNumber, isLeap)
print()
outputLeapYear(year, isLeap)
outputDaysOfMonth(days, monthNumber, year, isLeap)






    
