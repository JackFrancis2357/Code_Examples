library(rethinking)

f <- alist(
  y ~ dnorm( mu , sigma ),
  mu ~ dnorm( 0 , 10 ),
  sigma ~ dcauchy( 0 , 1 )
)

fit.stan <- map2stan( 
  f , 
  data=list(y=c(-1,1)) , 
  start=list(mu=0,sigma=1)
)

precis(fit.stan)
pairs(fit.stan)
