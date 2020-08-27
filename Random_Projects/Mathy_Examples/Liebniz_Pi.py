import numpy as np

current_estimate = 0
for i in range(1000):
    num = i * 2 + 1
    if i % 2 == 0:
        current_estimate += 1 / num
    else:
        current_estimate -= 1 / num
current_estimate *= 4

print(current_estimate)
print(np.pi)

# Chudnovsky Formula
for i in range(3000):
    numerator = np.math.factorial(6 * i) * (13591409 + (545140134 * i))
    denominator = np.math.factorial(3 * i) * (np.math.factorial(i) ** 3) * ((-640320) ** (3 * i))
    current_estimate += (numerator / denominator)
current_estimate *= (12 / ((640320) ** (3 / 2)))
pi_estimate = 1 / current_estimate

print(pi_estimate)
print(np.pi)
