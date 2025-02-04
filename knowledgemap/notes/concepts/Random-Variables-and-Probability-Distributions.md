# Random Variables

## Definition of Random Variable

<!-- ### Practical Definition
In machine learning, it suffices to think of a random variable simply as a 'variable', or a placeholder for a number or vector. There are notions of probability and randomness associated with it, but these can be associated with other constructs, like probability distributions.

For instance,

$$
y = 2z
$$
Means 'take the value that $z$ takes, and multiply it by $2$ to get $y$. There is no concept of 'randomness' yet introduced. -->

### Precise Definition

A random variable $X$ is a function from a sample space $\Omega$ to a set of outcomes $E$.

For instance, we can assign a random variable to the result of a dice roll, and call it $X$. In this case, the sample space is:
$$\Omega = \{1,2,3,4,5,6\}$$

The random variable $X$ is a function such that $X(\omega) = \omega$, for $\omega \in \Omega$.

<!-- It might seem redundant to define a random variable as a function, but it is conceptually useful because functions can take on multiple values depending on their input. If we think of $X$ as a function, it is easier to cope with the possibility that $X$ may take on more than one value. -->

### Operators on Random Variables
If we assign
$$
Y = 2X
$$

We can think of multiplication by $2$ as an operator on the function $X$ (An operator takes in a function and provides another function).

We are really saying that $Y$ is a new random variable (a new function), $y \mapsto Y(\omega)$, such that

$$
Y(\omega) = 2X(\omega) \quad \forall \omega.
$$

If $X$ is a random variable representing the value of a dice roll, $Y$ is a random variable representing twice the value of a dice roll.

### More notes on notation
#### Capital vs. Lowercase
While random variables are represented with capital letters, we typically use the corresponding lower case letter to denote a realization of that random variable. In math terms, we use $x$ to denote $X(\omega)$. 

$$
x = X(\omega)
$$

While $X$ is a function, $x$ is a value.

This is similar to how in mathematicals more generally, if $f$ refers to a function, then $f(x)$ refers to a value, namely, the output of $f$ when its input is $x$, although this distinction is [blurred frequently](https://en.wikipedia.org/wiki/Abuse_of_notation#Function_notation).

#### Bold vs unbolded
Bolded random variables and their values (realizations) simply indicate that the random variable is vector-valued.



### Sample Spaces in Machine Learning
The sample space is not usually referenced in machine learning. For instance, we might have a latent variable $\mathbf{Z}$ in a latent variable model. If $\mathbf{z} = \mathbf{Z}(\mathbf{w}) \in \mathbb{R}^d$, the sample space $\Omega$ is $\mathbb{R}^d$, and we think of $\mathbf{Z} : \Omega \rightarrow \mathbb{R}^d$ as $\mathbf{Z}(\omega) = \omega$.


## Probability Distributions
A probability distribution is a maps random variable ***values*** to densities. Formally, a random variable $\mathbf{X}$ is a function with an output domain (often $\mathbb{R}^d$), and the probability density function maps the output domain of $\mathbf{X}$ to density values in $\mathbb{R}$.
$$
p(\mathbf{x}) : \mathbb{R}^d \rightarrow \mathbb{R}.
$$

As an exercise in notation, this means we should also be able to write:
$$
p\left(\mathbf{X}(\mathbf{\omega})\right) : \mathbb{R}^d \rightarrow \mathbb{R}.
$$

We abbreviate "probability density function" as "PDF".


#### Note
It is not the case that a random variable has a single probability distribution, although we often reference a "true" probability distribution. Rather, a probability distribution is simply a mapping from a random variable's value to a density value.

### Notes on Notation
#### $Pr(x)$ vs $p(x)$
Typically, $Pr(A)$ refers to the probability of event $A$, while $p(x)$ refers to the value of the PDF at a data point $x$. Not everyone uses this notation, though.

#### Resolving function vs. value dilemma
We often use $f(x)$ to refer to the function $f$, instead of the value of $f$ at $x$. This is also true in statistics. We commonly use
$$
p(\mathbf{x})
$$

To refer to the probability distribution $p$, even though it should denote the density value of the probability distiribution at the point $\mathbf{x}$. This is used ubiquitiously, and perhaps the inclusion of $\mathbf{x}$ helps specify that the distribution's input are realizations of the random variable $X$. Sometimes, this is important because $p$ may represent a *family* of distributions, not just a single probability distribution.


#### Families of Probability Distributions
In machine learning, when we write something like $p_\theta$, we are typically referring to a *family* of probability distributions, not just a single distribution.

For instance, if we draw $\mathbf{x_1}, \ldots , \mathbf{x}_N$ independently from a data distribution, we can write

$$
p_\theta(\mathbf{x_1}, \ldots , \mathbf{x}_N) = \prod_{i=1}^N p_\theta(\mathbf{x_i}).
$$

In this case, the left hand side refers to the probability of observing $ \mathbf{x_1}, \ldots , \mathbf{x}_N $ according to the joint distribution given by the parameters $\theta$. We use $p_\theta$ to refer to both the joint *and* marginal distributions. They are intertwined by the rules of probability, e.g., the chain rule.




### Distributions 'over' random variables.
If we write
$$
\mathcal{N}_x(0,I)
$$
The $x$ in the subscript indicates that the distribution is "over" the random variable realization $x$, as opposed to another random variable. More precisely, $\mathcal{N}_x(0,I)$ is function mapping $x = X(\omega)$ to $\mathbb{R}$. The $x$ denotes what we use as the input to this function.

This is useful to disambiguate the input to the PDF when we have several PDFs.

#### Example

Suppose we have 

$$
p(\mathbf{x}) = \int \mathcal{N}_\mathbf{x}(f(\mathbf{z}), I) \cdot N_\mathbf{z}(0,I) d\mathbf{z}.
$$
In this case,


- $p(\mathbf{x})$ is a function mapping $\mathbf{x}$ to probability values.
- For a given input $\mathbf{x}$, we would substitute that value of $\mathbf{x}$ into $\mathcal{N}_\mathbf{x}(f(\mathbf{z}), I)$ to get a density value.
- The value of $\mathbf{z}$ we would use is determined by the integrand.


To evaluate $p(\mathbf{x})$ for a specific $\mathbf{x}$, we would:
1. Iterate through all values of $\mathbf{z}$
2. Plug in $f(\mathbf{z})$ for the these values to get the parameters (mean and variance) for the distribution $\mathcal{N}_\mathbf{x}$.
3. Plug in $\mathbf{x}$ into this distribution to get a probability density value.
4. Plug in $\mathbf{z}$ into $\mathcal{N}_\mathbf{z}(0,I)$ to get a probability density value
5. Multiply the two density values together (the outputs of the two normal distributions) and accumulate it over all $\mathbf{z}$ to evaluate the integral.

The parameters $f(\mathbf{z}), I$ are how we describe the function that is the probability distribution.

Last Reviewed: 1/31/25