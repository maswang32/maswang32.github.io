Last Reviewed: 1/25/25



We can ignore terms that are constant with regard to the distribution we are computing.
For instance, for a fixed x*,

p(z | x*)  = (p(x* | z) p(z)) / p(x*)

but we can ignore p(x*) since we are interested in a distribution with respect to z.
To get this distribution, we can evaluate p(x* | z) p(z) at all z and ensure it integrates to 1
by rescaling it by C
ignoring the need for p(x*) term (which is 1/C).

TO DO: Find notes about 'evidence' in Bayes


