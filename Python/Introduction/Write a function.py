# Returns a boolean value whether a given year is a leap year or not

def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0 and year % 400 != 0):
            return False
        elif (year % 400 == 0 and year % 100 != 0):
            return True
        else:
            return True
    else:
        return False