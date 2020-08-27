import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

test_mode = True

if test_mode:
    nsim = 10
else:
    nsim = 10 ** 5

# x range is from 0 to 3
# y range is from 0 to 1
# needle length is 1

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.axvline(x=0)
ax1.axvline(x=1)
ax1.axvline(x=2)
ax1.axvline(x=3)

number_of_crosses = 0


def animate(i):
    x = random.random() * 3
    y = random.random()
    angle = random.random() * 2 * math.pi
    x1, x2, x3 = -0.5 * np.cos(angle) + x, x, 0.5 * np.cos(angle) + x
    y1, y2, y3 = -0.5 * np.sin(angle) + y, y, 0.5 * np.sin(angle) + y
    ax1.plot([x1, x3], [y1, y3], 'g-')

    # Lets check if the needle crosses a line
    if x1 > 3 or x3 > 3:
        ax1.plot([x1, x3], [y1, y3], 'r-')
    elif x1 > 2:
        if x3 > 3:
            ax1.plot([x1, x3], [y1, y3], 'r-')
        elif x3 < 2:
            ax1.plot([x1, x3], [y1, y3], 'r-')
    elif x1 > 1:
        if x3 > 2:
            ax1.plot([x1, x3], [y1, y3], 'r-')
        elif x3 < 1:
            ax1.plot([x1, x3], [y1, y3], 'r-')
    elif x1 > 0:
        if x3 > 1:
            ax1.plot([x1, x3], [y1, y3], 'r-')
        elif x3 < 0:
            ax1.plot([x1, x3], [y1, y3], 'r-')
    elif x1 < 0 or x3 < 0:
        ax1.plot([x1, x3], [y1, y3], 'r-')


ani = animation.FuncAnimation(fig, animate, interval=100, frames=nsim)

plt.show()

# print(nsim / number_of_crosses * 2)
