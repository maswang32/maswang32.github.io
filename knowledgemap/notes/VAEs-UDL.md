# VAEs - UDL

<span style="color:blue">To Do: Organize</span>.

<span style="color:blue">To Do: Insert ELBO Math</span>.

## Introduction
- VAEs do not let you evaluate p(x)
- MLE training is not trivial, but can define a lower bound
- model an 'unobserved' latent variable, the thing that 'gives rise' to the image/sound
- p(x) = integral(P(x,z)dz) = integral(p(x|z)p(z)dz)
Example - Mixture of Gaussians, z describes which gaussian.

VAE - P(z) is N(O,I), and P(x|z) is N(f(z), s^2I)
In other words, z maps to a gaussian's mean, and the distribution is a marginalization of all these gaussians over z.

See image where one distribution is made up of as a 'marginalization' (sum) of gaussians

Generation: sample from P(z) then P(x|z)

Evaluating/maximizing p(x) slash sum(log(p(x)))is intractable.

A model that maximizes it could try to assign big probabilities to your data, without being restricted to 
integrating to 1.

Trying to restrict it to integrate to 1 is intractable.


Note:
p(z|x) is the 'posterior.' What could the latent variable be after observing x?
p(z) is the 'prior' on the latent variable.
p(x|z) is the 'likelihood'. This helps us evaluate the Posterior, since we want to see, for each value of z,
what is the probability we could have gotten that x? it's detective work.
To evaluate the posterior, Bayes Rule would say:

p(z|x) = p(x|z)p(z)/p(x).
But really, we only need the numerator, since we can make it integrate to 1, and p(x) does not determine the
relative probabilites of the z's.
1---Compute p(x|z) for each value of z
2---multiply by p(z)
3---normalize so the posterior p(z|x) sums to 1
There's a diagram of this in UDL.

p(x) is called the evidence
Last Reviewed: 1/19/25
