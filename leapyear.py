def leapyear(a):
    if a < 0:
        return "error"
    elif (int(a)%4 != 0):
        return "Year is not a leap year"
    elif a%100 != 0:
        return "This is a leap year!"