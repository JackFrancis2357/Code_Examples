import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# Rules of game. If < 2 neighbors, 1 -> 0. If > 3 neighbors 1 -> 0. If == 3 neighbors 0 -> 1

def compute_neighbor_edge(x, y, grid):
    # Corners first
    if x == 0 and y == 0:
        return grid[x + 1, y] + grid[x, y + 1] + grid[x + 1, y + 1]
    elif x == 0 and y == grid.shape[1] - 1:
        return grid[x, y - 1] + grid[x + 1, y - 1] + grid[x + 1, y]
    elif x == grid.shape[0] - 1 and y == 0:
        return grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y + 1]
    elif x == grid.shape[0] - 1 and y == grid.shape[1] - 1:
        return grid[x, y - 1] + grid[x - 1, y - 1] + grid[x - 1, y]
    elif x == 0:
        return grid[x + 1, y] + grid[x + 1, y - 1] + grid[x + 1, y + 1] + grid[x, y - 1] + grid[x, y + 1]
    elif x == grid.shape[0] - 1:
        return grid[x - 1, y] + grid[x - 1, y + 1] + grid[x - 1, y - 1] + grid[x, y - 1] + grid[x, y + 1]
    elif y == 0:
        return grid[x + 1, y + 1] + grid[x, y + 1] + grid[x - 1, y + 1] + grid[x + 1, y] + grid[x - 1, y]
    elif y == grid.shape[1] - 1:
        return grid[x + 1, y - 1] + grid[x, y - 1] + grid[x - 1, y - 1] + grid[x + 1, y] + grid[x - 1, y]


def game_of_life(initial_state, row, col):
    next_state = np.zeros((row, col), dtype=np.int8)
    for i in range(initial_state.shape[0]):
        for j in range(initial_state.shape[1]):
            if i == 0 or i == initial_state.shape[0] - 1 or j == 0 or j == initial_state.shape[1] - 1:
                running_sum = compute_neighbor_edge(i, j, initial_state)
            else:
                running_sum = initial_state[i - 1, j] + initial_state[i - 1, j + 1] + initial_state[i, j + 1] + \
                              initial_state[i + 1, j + 1] + initial_state[i + 1, j] + initial_state[i + 1, j - 1] + \
                              initial_state[i, j - 1] + initial_state[i - 1, j - 1]
            if running_sum < 2 or running_sum > 4:
                next_state[i, j] = 0
            elif running_sum == 3 or running_sum == 4:
                next_state[i, j] = 1
            else:
                next_state[i, j] = initial_state[i, j]
    return next_state


row_size = 100
col_size = 100
state = np.random.randint(0, 2, (row_size, col_size))

ims = []
for i in range(150):
    state = game_of_life(state, row_size, col_size)
    ims.append([plt.imshow(state)])

fig = plt.figure()
interval = 300
im_ani = animation.ArtistAnimation(fig, ims, interval=interval, blit=True)
plt.show()
