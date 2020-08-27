def divisor_check(number):
    divisors = []
    for j in range(1, number + 1):
        if number % j == 0:
            divisors.append(j)
    return divisors


print (divisor_check(100))
