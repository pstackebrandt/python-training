# Leap year: leap-year.py
# Code by Peter Stackebrandt

# Create a simple leap year test(Schaltjahr).
# Task by Kofler:Python.-2024, 9.7. W1 p. 135, 151

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






    
