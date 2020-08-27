# Model

# D ~ N(mu, sigma)
# mu ~ N(10, 5)
# sigma ~ U(0,10)
mu = rep(0, 1000)
sigma = rep(0, 1000)

for(i in 1:1000){
  mu[i] = rnorm(1, 100, 25)
  sigma[i] = runif(1, 0, 10)
}

posterior_samples = rep(0,1000)
for(i in 1:1000){
  posterior_samples[i] = rnorm(1, mu[i], sigma[i])
}

plot(posterior_samples)
hist(posterior_samples)

x = cars$speed

# Model
# Dist ~ N(mu, sigma)
# mu = alpha + beta * cars$speed

alpha = rep(0,1000)
beta = rep(0, 1000)
mu = matrix(0, nrow = 1000, ncol = 1000)
post = matrix(0,nrow = 1000, ncol = 1000)

for(i in 1:1000){
  alpha[i] = rnorm(1, 10, 1)
  beta[i] = rnorm(1, 0, 1)
  sigma[i] = runif(1, 0, 10)
  mu[i,] = alpha[i] + beta[i] * cars$speed
  post[i,] = rnorm(1,mu[i,], sigma[i])
}

hist(alpha)
hist(beta)
