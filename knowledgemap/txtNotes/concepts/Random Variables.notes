Last Reviewed: 1/19/25

Random Variable x - a variable that can take on different values. e.g, result of dice roll.
Distribution Pr(x) - maps r.v. values to densities.
N_x(0,I) - describes the distribution of x - as opposed to some other random variable.
N_x(f(z), I) is a function mapping x to probability values, not some other random variable.

Example:
Suppose we have Pr(x) = integral( N_x(f(z), I), N_z(0,I)) dz.
Pr(x) is a function mapping x to probabilities
On the right hand side, for a given input x,
We would substitute that value of x in for N_x(x|z).
The value of z we would use is determined by the integrand.

To evaluate Pr(x=0.5), we would
1. Iterate through all values of z
2. Plug in f(z) for the these values to get the parameters (mean and variance) for the distribution
3. Plug in x into this distribution to get a probability value.
4. Plug in z into N_z(0,I) to get a probability value
5. Multiply the outputs of the two normals and add it to the integral value.

In other words, the 'x' in N_x describes what we use for the function's input.
The parameters are how we describe the function.