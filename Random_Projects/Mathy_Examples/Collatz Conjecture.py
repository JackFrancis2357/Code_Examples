counter = 0
maxcounter = 0


def collatz(number):
    if number % 2 == 0:
        number /= 2
    else:
        number = (3 * number + 1)
    return number


for j in range(1, 10000):
    i = j
    while not i == 1:
        collatz(i)
        i = collatz(i)
        counter += 1
    print (j, counter)
    if counter > maxcounter:
        maxcounter = counter
        maxvalue = j
    counter = 0

print (maxvalue, maxcounter)
