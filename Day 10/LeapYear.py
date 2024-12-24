# find a year is leap year or not

def checkLeapYear(year):
    """Function checks a year is Leap or not"""
    if year%4==0:
        if year%400==0 and year%100==0:
            return True
    return False

year = int(input("Enter a year: "))
if checkLeapYear(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
