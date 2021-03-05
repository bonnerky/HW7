def fizzbuzz (a):
    if a%3 == 0:
        s = str(a) + " fizz"
        return s
    elif a%5 == 0:
        s = str(a) + " buzz"
        return s
    else:
        return str(a)