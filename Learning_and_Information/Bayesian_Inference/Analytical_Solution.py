import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

data = np.random.randn(50)
ax = plt.subplot()
sns.distplot(data, kde=False, ax=ax)
_ = ax.set(title='Histogram of observed data', xlabel='x', ylabel='# observations')
plt.show()


def calc_posterior_analytical(data, x, mu_0, sigma_0):
    sigma = 2.
    n = len(data)
    mu_post = (mu_0 / sigma_0 ** 2 + data.sum() / sigma ** 2) / (1. / sigma_0 ** 2 + n / sigma ** 2)
    sigma_post = (1. / sigma_0 ** 2 + n / sigma ** 2) ** -1
    return norm(mu_post, np.sqrt(sigma_post)).pdf(x)


prior_mean = 10
prior_sigma = 10
ax = plt.subplot()
x = np.linspace(-10, 10, 1000)
posterior = calc_posterior_analytical(data, x, prior_mean, prior_sigma)
ax.plot(x, posterior)
ax.set(xlabel='mu', ylabel='belief', title='Analytical posterior');
sns.despine()
plt.show()
print(posterior)
