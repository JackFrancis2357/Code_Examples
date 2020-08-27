target = function(x){
  if(x<0){
    return(0)}
  else {
    return(exp(-x))
  }
}

target(1)

x = rep(0,1000)
x[1] = 3     #this is just a starting value, which I've set arbitrarily to 3
for(i in 2:1000){
  currentx = x[i-1]
  proposedx = currentx + rnorm(1,mean=0,sd=1)
  A = target(proposedx)/target(currentx) 
  if(runif(1)<A){
    x[i] = proposedx       # accept move with probabily min(1,A)
  } else {
    x[i] = currentx        # otherwise "reject" move, and stay where we are
  }
}

hist(x)