def primecheck(number):
    x = number
    for i in range(2, x):
        if number % i == 0:
            return False
        else: continue
    return True

for i in range(1,100):
    print (primecheck(i))

