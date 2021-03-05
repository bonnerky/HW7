def fizzbuzz (a):
    if a%3 == 0 and a%5 == 0:
        s = str(a) + " fizzbuzz"
        return s   
    elif a%3 == 0:
        s = str(a) + " fizz"
        return s
    elif a%5 == 0:
        s = str(a) + " buzz"
        return s
    else:
        return str(a)

a = 1
while a < 101:
    print(fizzbuzz(a))
    a += 1