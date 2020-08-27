data(chimpanzees)

# don't want any variables with NAs
d <- list( 
  pulled_left = chimpanzees$pulled_left ,
  prosoc_left = chimpanzees$prosoc_left ,
  condition = chimpanzees$condition ,
  actor = as.integer( chimpanzees$actor ) ,
  blockid = as.integer( chimpanzees$block )
)

# RStan fit
m2 <- map2stan(
  alist(
    pulled_left ~ dbinom(1,theta),
    logit(theta) <- a + bp*prosoc_left + bpc*condition*prosoc_left ,
    a ~ dnorm(0,10),
    bp ~ dnorm(0,10),
    bpc ~ dnorm(0,10)
  ) ,
  data=d, chains=2, cores=1 )

precis(m2)
summary(m2)
plot(m2)
pairs(m2)

# now RStan fit of model with varying intercepts on actor
m3 <- map2stan(
  alist(
    pulled_left ~ dbinom(1,theta),
    logit(theta) <- a + aj[actor] + bp*prosoc_left + bpc*condition*prosoc_left,
    aj[actor] ~ dnorm( 0 , sigma_actor ),
    a ~ dnorm(0,10),
    bp ~ dnorm(0,10),
    bpc ~ dnorm(0,10),
    sigma_actor ~ dcauchy(0,1)
  ) ,
  data=d,
  iter=5000 , warmup=1000 , chains=2 , cores=1 )

precis(m3)
plot(m3)
pairs(m3)

# varying intercepts on actor and experimental block
m4 <- map2stan(
  alist(
    pulled_left ~ dbinom(1,theta),
    logit(theta) <- a + aj + ak + bp*prosoc_left + bpc*condition*prosoc_left,
    aj[actor] ~ dnorm( 0 , sigma_actor ),
    ak[blockid] ~ dnorm( 0 , sigma_block ),
    a ~ dnorm(0,10),
    bp ~ dnorm(0,10),
    bpc ~ dnorm(0,10),
    sigma_actor ~ dcauchy(0,1),
    sigma_block ~ dcauchy(0,1)
  ) ,
  data=d,
  iter=5000 , warmup=1000 , chains=2 , cores=1 )

precis(m4)
summary(m4)
plot(m4)

# compare posterior means
coeftab(m2,m3,m4)
plot(coeftab(m2,m3,m4))

# show WAIC for m2,m3,m4
compare(m2,m3,m4)
plot(compare(m2,m3,m4))

###########
# varying slopes models

# varying slopes on actor
# also demonstrates use of multiple linear models
# see Chapter 13 for discussion
m5 <- map2stan(
  alist(
    # likeliood
    pulled_left ~ dbinom(1,p),
    
    # linear models
    logit(p) <- A + (BP + BPC*condition)*prosoc_left,
    A <- a + a_actor[actor],
    BP <- bp + bp_actor[actor],
    BPC <- bpc + bpc_actor[actor],
    
    # adaptive prior
    c(a_actor,bp_actor,bpc_actor)[actor] ~
      dmvnorm2(0,sigma_actor,Rho_actor),
    
    # fixed priors
    c(a,bp,bpc) ~ dnorm(0,1),
    sigma_actor ~ dcauchy(0,2),
    Rho_actor ~ dlkjcorr(4)
  ) , data=d , iter=5000 , warmup=1000 , chains=3 , cores=3 )

# same model but with non-centered parameterization
# see Chapter 13 for explanation and more elaborate example

m6 <- map2stan(
  alist(
    # likeliood
    pulled_left ~ dbinom(1,p),
    
    # linear models
    logit(p) <- A + (BP + BPC*condition)*prosoc_left,
    A <- a + a_actor[actor],
    BP <- bp + bp_actor[actor],
    BPC <- bpc + bpc_actor[actor],
    
    # adaptive prior - non-centered
    c(a_actor,bp_actor,bpc_actor)[actor] ~
      dmvnormNC(sigma_actor,Rho_actor),
    
    # fixed priors
    c(a,bp,bpc) ~ dnorm(0,1),
    sigma_actor ~ dcauchy(0,2),
    Rho_actor ~ dlkjcorr(4)
  ) , data=d , iter=5000 , warmup=1000 , chains=3 , cores=3 )

###########
# Imputation example

# simulate data:
#  linear regression with two predictors
#  both predictors have valules missing at random
N <- 100
N_miss <- 10
x1 <- rnorm( N )
x2 <- rnorm( N )
y <- rnorm( N , 2*x1 - 0.5*x2 , 1 )
x1[ sample(1:N,size=N_miss) ] <- NA
x2[ sample(1:N,size=N_miss) ] <- NA

# formula with distributions assigned to both predictors
f <- alist(
  y ~ dnorm( mu , sigma ),
  mu <- a + b1*x1 + b2*x2,
  x1 ~ dnorm( mu_x1, sigma_x1 ),
  x2 ~ dnorm( mu_x2, sigma_x2 ),
  a ~ dnorm( 0 , 100 ),
  c(b1,b2) ~ dnorm( 0  , 10 ),
  c(mu_x1,mu_x2) ~ dnorm( 0 , 100 ),
  c(sigma_x1,sigma_x2) ~ dcauchy(0,2),
  sigma ~ dcauchy(0,2)
)

m <- map2stan( f , data=list(y=y,x1=x1,x2=x2) , sample=TRUE )

# show observed outcomes against retrodicted outcomes
# cases with missing values shown with red posterior intervals
v <- link(m)
mu <- apply( v , 2 , mean )
ci <- apply( v , 2 , PI )
plot( y ~ mu )
cicols <- ifelse( is.na(x1) | is.na(x2) , "red" , "gray" )
for( i in 1:N ) lines( ci[,i] , rep(y[i],2) , col=cicols[i] )

## End(Not run)
