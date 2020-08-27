# 11 ones
# 18 twos
# 39 threes
# 44 fours
# 21 fives
# 11 sixes

import numpy as np
import matplotlib.pyplot as plt


def play_game(current_points, current_cost, current_prize):
    roll_sum = np.sum(
        np.random.choice(np.arange(1, 7), size=8, p=[11 / 144, 18 / 144, 39 / 144, 44 / 144, 21 / 144, 11 / 144]))

    if 18 <= roll_sum <= 21 or 35 <= roll_sum <= 38:
        return current_points, current_cost, current_prize + 1
    elif roll_sum == 29:
        return current_points, current_cost * 2, current_prize
    elif 22 <= roll_sum <= 34:
        return current_points, current_cost, current_prize
    elif roll_sum == 17 or roll_sum == 39 or roll_sum == 40:
        return current_points + 5, current_cost, current_prize
    elif roll_sum == 16:
        return current_points + 10, current_cost, current_prize
    elif roll_sum == 15 or roll_sum == 41:
        return current_points + 15, current_cost, current_prize
    elif roll_sum == 14 or roll_sum == 42:
        return current_points + 20, current_cost, current_prize
    elif roll_sum == 11 or roll_sum == 45:
        return current_points + 30, current_cost, current_prize
    elif roll_sum == 10 or roll_sum == 12 or roll_sum == 13 or roll_sum == 43 or roll_sum == 44 or roll_sum == 46:
        return current_points + 50, current_cost, current_prize
    elif roll_sum == 8 or roll_sum == 9 or roll_sum == 47 or roll_sum == 48:
        return current_points + 100, current_cost, current_prize
    else:
        print(roll_sum)


num_simulations = 100
times_played = []

for i in range(num_simulations):
    points = 0
    cost = 1
    prize = 1
    game_play = 0
    total_cost = 0
    while points < 100:
        total_cost += cost
        game_play += 1
        points, cost, prize = play_game(points, cost, prize)
    times_played.append(game_play)

plt.hist(times_played)
plt.show()

print(game_play)
print(points)
print(cost)
print()
