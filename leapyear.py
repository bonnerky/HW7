def leapyear(a):
    if a < 0:
        return "error"
    elif (int(a)%4 != 0):
        return "Year is not a leap year"