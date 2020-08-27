import matplotlib.pyplot as plt
import numpy as np

number_of_people = 100
number_of_simulations = 10000
occurences = np.zeros((number_of_people, 2))
for i in range(number_of_people):
    occurences[i, 0] = i

for simulation in range(number_of_simulations):
    counter = 0
    population = []
    for person in range(1, number_of_people):
        age = np.random.randint(1, 366)
        population.append(age)
        if len(population) > len(set(population)):
            occurences[person, 1] += 1

for person in range(number_of_people):
    occurences[person, 1] = occurences[person, 1] / number_of_simulations
print(occurences)

plt.plot(occurences[:, 0], occurences[:, 1])
plt.axhline(y=0.5)
plt.show()
