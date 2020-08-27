import numpy as np

# Let's create some silly data following y = 2x + 7

x = np.zeros(shape=(30, 2))
y = np.zeros(shape=(30, 1))

for i in range(30):
    x[i][0] = 1
    x[i][1] = i
    y[i] = 2 * i + 56

guess = np.zeros(shape=(2, 1))

for i in range(1000):
    x_test = np.dot(x, guess)
    loss = x_test - y
    cost = np.sum(loss**2) / (2 * x_test.shape[0])
    print('Iteration {} Cost {}'.format(i, cost))
    gradient = np.dot(np.transpose(x), loss) / x_test.shape[0]
    guess = guess - 0.005 * gradient

print(guess)