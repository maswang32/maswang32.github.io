# Downsampling and Stretching
Lots of math here. You can reprove this by hand from Jensen's inequality or look at your notes

Basically, start with log(p(x)).
---Then express it using a latent variable model decomposition
---choose an arbitrary q(z) as your 'weighting'
int(  log(    q(z) * p(x,z)/q(z)         )  dz)
---apply Jensen's inequality
when you get to p(x,z) split it up into p(z|x) and p(x)
that will let you take out p(x), and also give you a KL term

ELBO = log(p(x)) - KL(q(z), p(z|x))) (this KL is assuming q is 'ground truth')

Maximizing p(x) with respect to the parameters for q(z) and p(z|x) involves expectation maximization, this means
---can improve ELBO's lower bound by changing p(z|x) slash p(x|z)'s parametrization
OR
---can make ELBO bound more tight by changing q(z)'s parametrization
Last Reviewed: 1/19/25