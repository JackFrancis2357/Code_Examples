import numpy as np


def wand_1_battle(wand_1, wand_1_alive, wand_2_alive, wand_3_alive):
    if not wand_1_alive:
        pass
    elif wand_3_alive:
        if np.random.rand() > wand_1:
            pass
        else:
            wand_3_alive = False
    else:
        if np.random.rand() > wand_1:
            pass
        else:
            wand_2_alive = False

    return wand_2_alive, wand_3_alive


def wand_2_battle(wand_1, wand_2, wand_3, wand_1_alive, wand_2_alive, wand_3_alive):
    if not wand_2_alive:
        pass
    elif wand_1 > wand_3 and wand_1_alive:
        if np.random.rand() > wand_2:
            pass
        else:
            wand_1_alive = False
    elif wand_1_alive and not wand_3_alive:
        if np.random.rand() > wand_2:
            pass
        else:
            wand_1_alive = False
    else:
        if np.random.rand() > 0.7:
            pass
        else:
            wand_3_alive = False
    return wand_1_alive, wand_3_alive


def wand_3_battle(wand_1, wand_2, wand_3, wand_1_alive, wand_2_alive, wand_3_alive):
    if not wand_3_alive:
        pass
    elif wand_1 > wand_2 and wand_1_alive:
        if np.random.rand() > wand_3:
            pass
        else:
            wand_1_alive = False
    elif wand_1_alive and not wand_2_alive:
        if np.random.rand() > wand_3:
            pass
        else:
            wand_1_alive = False
    else:
        if np.random.rand() > wand_3:
            pass
        else:
            wand_2_alive = False
    return wand_1_alive, wand_2_alive

# Lets battle
# Effectiveness of the wands and other params
# Wand 3 needs to be higher than Wand 2
wand_1 = 0.6
wand_2 = 0.7
wand_3 = 0.9

wand_1_wins = 0
wand_2_wins = 0
wand_3_wins = 0
cats = 0

Nsim = 10000
for battle in range(Nsim):
    wand_1_alive, wand_2_alive, wand_3_alive = True, True, True
    while wand_1_alive + wand_2_alive + wand_3_alive > 1:
        wand_2_alive, wand_3_alive = wand_1_battle(wand_1, wand_1_alive, wand_2_alive, wand_3_alive)
        wand_1_alive, wand_3_alive = wand_2_battle(wand_1, wand_2, wand_3, wand_1_alive, wand_2_alive, wand_3_alive)
        wand_1_alive, wand_2_alive = wand_3_battle(wand_1, wand_3, wand_3, wand_1_alive, wand_2_alive, wand_3_alive)
        if wand_1_alive + wand_2_alive + wand_3_alive == 3:
            wand_1_alive, wand_2_alive, wand_3_alive = False, False, False
    if wand_1_alive:
        wand_1_wins += 1
    elif wand_2_alive:
        wand_2_wins += 1
    elif wand_3_alive:
        wand_3_wins += 1
    else:
        cats += 1

print(wand_1_wins/Nsim)
print(wand_2_wins/Nsim)
print(wand_3_wins/Nsim)
print(cats/Nsim)