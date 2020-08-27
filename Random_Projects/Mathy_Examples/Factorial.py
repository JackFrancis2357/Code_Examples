def factorial(number):
    factorial = 1
    if number == 0:
        factorial = 1
    else:
        for i in range(2, number + 1):
            factorial *= i
    return factorial


for i in range(1, 100):
    print (factorial(i))
