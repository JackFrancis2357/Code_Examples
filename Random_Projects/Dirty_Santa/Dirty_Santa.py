import random

list_of_names = []

for _ in range(len(list_of_names)):
    person = random.choice(list_of_names)
    print(person)
    for person2 in list_of_names:
        if person == person2:
            counter = list_of_names.index(person2)
            del list_of_names[counter]
