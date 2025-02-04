
# SDEs for Generative Modeling

## Forward-Time Diffusion

For a noise-conditional score network, there is a finite number of noise levels.

As the number of diffusion timesteps approaches infinity ($L \rightarrow \infty$), the noise level becomes a continuous-time stochastic process, where noise is added continuously.


We have:

$$
d\mathbf{x} = \mathbf{f}(\mathbf{x}, t) dt + g(t)d\mathbf{w}
$$

$d\mathbf{w}$ can be viewed as infinitesimal white noise, and characterizes a [Wiener Process](https://masonlwang.com/knowledgemap/notes/concepts/wiener-process).

$\mathbf{f}$ is a vector-valued function representing the *drift coefficient* and $g(t)$ is a scalar-valued function called the *diffusion coefficient*.

We can imagine applying this diffusion process to our data. As $t$ changes, the distribution of our data changes. We can use $p_t(\mathbf{x})$ to denote the probability distribution of our data at diffusion time $t$, where $t \in [0,T]$. The data distribution (with no diffusion) is $p_0(\mathbf{x})$.

In addition, we can let $\mathbf{X}_t$ be a random variable representing the value of a datapoint at diffusion time $t$, and use $\mathbf{x}_t$ to represent a realization of $\mathbf{X}_t$.

We choose our diffusion process so that $p_T$ does not depend on $p_0$.

#### Extra Thoughts
- In DDPMs, the *drift coefficient* $\mathbf{f}(\mathbf{x}, t)$ would be analogous to $\sqrt{1-\beta_t}$ when defining the forward process. It is kind of like the derivative of the coefficient on $\mathbf{x}_0$.
- in DDPMs, the diffusion coefficient is analogous to $\sqrt{\beta_t}$. It is kind of like the derivative of $\sigma_i$ or the derivative of the coefficent on the noise term in DDPMs. It represents the variance of the noise added at each step.


### Choices of $\mathbf{f}(\mathbf{x},t), g(t)$

We can choose the diffusion and drift coefficients as hyperparameters. For instance, we can choose a forward diffusion process:

$$
d\mathbf{x} = e^t d\mathbf{w}
$$
Which means that the variance grows exponentially as time increases, and is similar to choosing a geometric progression of noise scales $\sigma_1, \ldots, \sigma_L$. For instance, the Variance Exploding SDE, the Variance Preserving SDE, and the sub-VP SDE work well for generating images.

## Reverse-Time Diffusion

The reverse diffusion process is defined as:

$$
d\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g^2(t)\nabla_\mathbf{x} \log(p_t(\mathbf{x}))\right] dt + g(t)d\mathbf{\bar{w}}
$$

If we know the drift and diffusion coefficients (which are from the forward process), and can approximate the score function (the gradient of the data distributions at time $t$), then we can compute the reverse-time SDE.

<!-- When we integrate from $T$ to $t$, we should get the marginal distributions for $p_t(\mathbf{x})$ determined by forward-time diffusion, if we start from a datapoint sampled from $p_T$. -->

We can sample from any marginal distribution $p_t$ (determined by the forward process) by sampling from $p_T$ (which should be doable, since this should approximate an easy-to-sample from distribution), then by integrating from $T$ to $t$. By integrating all the way to $t=0$, we should be able to generate a data sample.

#### Extra Thoughts
- Note that $dt$ represents an infinitesimal *negative* time step, since we are integrating from higher $t$ to lower $t$.
- **What is a Reverse-Time SDE?** In this case, $\mathbf{\bar{w}}$ is described as 'reverse-time brownian motion'. In practice, $d\mathbf{\bar{w}}$ is Gaussian Noise, just like $d\mathbf{w}$ in the forward process.
<!-- Technically, we can view it like this:

$$
d \mathbf{\bar{w}} \sim \mathcal{N}(0, ds)
$$ -->
<!-- 


, which is defined as:



$$
\mathbf{\bar{w}}_t = \mathbf{w}_T - \mathbf{w}_{T-t}
$$

We can also view -->


<!-- Where $s = T - t$, and thus $ds = -dt$. -->


<!-- 
We can use $p_t(\mathbf{x})$ to define the probability distribution of $\mathbf{X_t}$, according to the data distribution, which is $p_0(x)$ -->




## Learning the Score Function
We would like to fit the score function such that

$$
\mathbf{s}_\theta(\mathbf{x}, t) \approx \nabla_\mathbf{x} \log p_{t} (\mathbf{x})
$$

This should be a continuous weighted sum of:
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$
Where $\lambda(t)$ is a weighting function. We would like to balance the losses across time, so we choose

$$
\lambda(t) \propto 1/
\mathbb{E}_{p_t(\mathbf{x})}
\lVert
\nabla_{\mathbf{x}_t}
\log p_{t} (\mathbf{x}_t \mid \mathbf{x}_0) \rVert^2_2
$$

To implement this weighting, we also rescale the outputs of the network, so its outputs are on the same scale across time-steps.

In addition, we use the exponential moving average of the weights during sampling.

#### Additional Notes from Mason:
- The expectation here is proportional to the expected amount of noise added. 

- Note that in DDPM, the network is always predicting samples from $\mathcal{N}(0, I)$ no matter the timestep, which is similar to rescaling the outputs of the network in DDIM.


We can use denoising score matching to optimize this objective.

### Actual Optimization
We have
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_{\sigma_t} (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$

We can estimate this objective as 

$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x_0} \sim p_0(\mathbf{x})}
\mathbb{E}_{\mathbf{x_t} p_t(\mathbf{x_t} \mid \mathbf{x_0})}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x_t}, t)  \rVert^2_2
\right]
\right]$$

#### Additional Thoughts
- We would like the score function to fit $\nabla_\mathbf{x_t} \log p_{t} (\mathbf{x_t})$, but this distribution may be complex and multimodal. However, $\log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0)$ is just Gaussian.

- Since the score function we are fitting does not see $\mathbf{x_0}$, it will fit an expectation over all possible $\mathbf{x_0}$, which will approximate the score function of $p_t(\mathbf{x_t})$.
- The probability distribution of $p_t(\mathbf{x_t})$ is a mixture of Gaussians, which means that the conditional distribution $\log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0)$ locally approximates $\log p_{t} (\mathbf{x_t})$ at the point $\mathbf{x_t}$.

##### A derivation that both objectives are equivalent
Our intended objective is:
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_{\sigma_t} (\mathbf{x}) -
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right]
$$

We would like to show this objective is equivalent:
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x_0} \sim p_0(\mathbf{x})}
\mathbb{E}_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x_t}, t)  \rVert^2_2
\right]
\right]
$$


###### Lemma
We first show that we can estimate the marginal distribution as an expecation of the conditionals:

$$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) = \mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0})
\right]
$$

<span style="color:blue">To Do: Prove this Lemma</span>.

In other words, we can approximate the marginal score function by sampling from the posterior, and aggregating the score esimates that we can from single samples.

###### Bias Variance Decomposition
By the law of total variance, we have:
$$
\mathbb{E} \| Z - a \|^2_2 =  \| \mathbb{E}[Z] - a \|^2_2 + \mathbb{E} \left[ \| Z - \mathbb{E}[Z] \|^2_2 \right] \\[10pt]
= \| \mathbb{E}[Z] - a \|^2_2 + \operatorname{Var}(Z)
$$
For any random variable $Z$.
<span style="color:blue">To Do: Prove this Decomposition</span>.

###### Another Equality
Consider the new expression
$$
\tag{*}
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]
$$
By the bias-variance decomposition, this is equal to
$$
\left\lVert
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0})
\right] - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 +
\operatorname{Var}\left[\nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0})\right] = \\[10pt]
\left\lVert
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0})
\right] - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C
$$
Where we are use $C$ to denote the variance expression, which is constant given the forward process and does not depend on model parameters $\theta$. By the Lemma, this is equal to
$$
\tag{**}
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C 
$$
Which is our score matching objective for a single timestep, plus a constant.
###### Wrapping in expectation
Let us wrap both starred expressions (which we have proven to be equal) in an expectation over $\mathbf{x}_t$:

$$
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t)}
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] = \\[10pt]
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right]
$$
By using the chain rule:
$$
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] = \\[10pt]
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right]
$$
If we wrap both in another expectation over $t$, and multiply by $\lambda(t)$, we get
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]\right] = \\[10pt]
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 + C \right] \right]
$$
The $C$ term can be taken out of the inner expectation, and remains constant with repsect to $\theta$ when it is taken outside of the outer expecation:
$$
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0)}
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t \mid \mathbf{x}_0)}
\left[
\left\lVert
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right]\right] = \\[10pt]
\mathbb{E}_{t \sim \mathcal{U}(0,T)}
\lambda(t)
\left[
\mathbb{E}_{\mathbf{x}_t\sim p(\mathbf{x}_t)}\left[
\left\lVert
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) - s_\theta(\mathbf{x}_t, t) \right\rVert^2_2 \right] \right] + C_2
$$
The left hand side is the objective that we train with, and the right hand side is the optimization objective. Thus, we have that the two optimization objectives are equivalent - they differ by a constant that does not depend on our parameters $\theta$.
<!-- $$
\nabla_{\mathbf{x}_t} \log p_t(\mathbf{x_t}) = \mathbb{E}_{\mathbf{x}_0\sim p(\mathbf{x}_0 \mid \mathbf{x_t})} \left[
    \nabla_{\mathbf{x}_t} \log p(\mathbf{x_t} \mid \mathbf{x_0})
\right]
$$



####
Let us narrow in on this term:
$$
\mathbb{E}_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x_t}, t)  \rVert^2_2
\right]
$$


Applying it:
$$
\mathbb{E}_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}
\left[
\lVert
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0) -
\mathbf{s}_\theta(\mathbf{x_t}, t)  \rVert^2_2
\right] = \\[10pt]
\left\lVert
\mathbb{E}_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}\left[
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0)\right] -
\mathbf{s}_\theta(\mathbf{x_t}, t) \right\rVert^2_2 + \operatorname{Var}\left[ p(\mathbf{x}_t \mid \mathbf{x}_0) \right]
$$
Let's analyze one of the terms further:
$$
\mathbb{E}_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}\left[
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0)\right] = 
\int_{\mathbf{x_t} \sim p_t(\mathbf{x_t} \mid \mathbf{x_0})}\left[
\nabla_\mathbf{x} \log p_{t} (\mathbf{x_t} \mid \mathbf{x}_0)\right] 
$$ -->

### 'Likelihood' Weighting

If $\lambda(t)$ = $g^2(t)$, we have that

$$
D_{\text{KL}}\left(p_0(\mathbf{x}) \right) \| p_\theta(\mathbf{x})) = \frac{T}{2} \mathbb{E}_{t \sim \mathcal{U}(0,T)}
\mathbb{E}_{\mathbf{x} \sim p_t(\mathbf{x})}
\left[
\lambda(t)
\lVert
\nabla_\mathbf{x} \log p_{\sigma_t} (\mathbf{x}) - 
\mathbf{s}_\theta(\mathbf{x}, t)  \rVert^2_2
\right] + \\ D_{\text{KL}}\left(p_T\left(\mathbf{x}_t\right) \| \pi \left(\mathbf{x}_T\right) \right)
$$

Where $p_\theta(\mathbf{x})$ is the distribution we get for $\mathbf{x}_0$ we get using our estimated score function, and $\pi$ is a simple distribution that it is easy to sample from.


## Solving the Reverse-Time SDE

### The Integral
To generate samples, we can evaluate the reverse-time SDE. This is as simple as coming up with a numerical approximation to the integral of the reverse-time SDE process:

$$
d\mathbf{x} = \left[\mathbf{f}(\mathbf{x},t) - g^2(t)\nabla_\mathbf{x} \log(p_t(\mathbf{x}))\right] dt + g(t)d\mathbf{\bar{w}}
$$

##### Additional Notes
We can express our SDE in integral form:
$$
\mathbf{x_t} = \mathbf{x}_{t_0} + \int_{t_0}^t \left[\mathbf{f}(\mathbf{x},s) - g^2(s)\nabla_\mathbf{x} \log(p_s(\mathbf{x}))\right] ds + \int_{t_0}^t g(s)d\mathbf{\bar{w}}(s)
$$

Where
$$
d\mathbf{\bar{w}}(s) = \mathcal{N}(0, ds) ds
$$

<span style="color:blue">Question - can we get here by intergrating both sides of the SDE? If so, how?</span>.

Particularly, to get a sample from the marginal distribution, we can evaluate

$$
\mathbf{x}_t = \mathbf{x}_T + \int_{T}^t \left[\mathbf{f}(\mathbf{x},s) - g^2(s)\nabla_\mathbf{x} \log(p_s(\mathbf{x}))\right] ds + \int_{T}^t g(s)d\mathbf{\bar{w}}(s)
$$

Since we can sample $\mathbf{x}_T$ in closed form.

Finally, to generate a sample from the data distribution, we are interested in $\mathbf{x}_0$. This be obtained by setting $t=0$ in the above equation.

### Numerical Methods
Choose a small $\Delta t < 0$.

Then perform this process:

1. $$\mathbf{x}_T \sim \pi$$

2. $$
\mathbf{x}_{t + \Delta t} = \mathbf{x}_t + \left[ f(\mathbf{x}_t,t) - g^2(t) s_\theta(\mathbf{x}_t, t) \right] \Delta t + g(t)\mathbf{z}_t\sqrt{| \Delta t |}$$

Where $\mathbf{z}_t \sim \mathcal{N}(0, I)$. 

##### Additional Notes
-Note that the last term on the right side is a way to sample from $\mathcal{N}(0, | \Delta t |)$.

-This is similar to Langevin Sampling or "noisy gradient descent" for when time was not continuous.

#### Predictor-Corrector Methods
The predictor chooses a step size $\Delta t$, then predicts $\mathbf{x}_{t + \Delta t}$ based on $\mathbf{x}_{t}$. Then, we run several 'corrector' steps to improve our sample from $p_{t + \Delta t}$, using our estimate of its score function $\mathbf{s}_\theta(\mathbf{x}_{t + \Delta t}, t + \Delta t)$. We do this before moving on to the next time step.

This is similar to the discrete-time case, where we optimize the score at each noise level before moving to the next noise level.

## ODE Version

We can change the SDE into an ODE without changing its marginal distributions $p_t(\mathbf{x}_t)$. The formula is this:

$$
d\mathbf{x} = \left[f(\mathbf{x}, t) - \frac{1}{2} g^2(t)\nabla_\mathbf{x} \log p_t(\mathbf{x}_t) \right] dt
$$

ODE trajectories are actually smoother, and this process is invertible. We can directly convert $\mathbf{x}_0$ to $\mathbf{x}_T$ and convert it back. 

This is a special case of a continuous time neural ODE and a normalizing flow, and allows for exact likelihood computation.

## Inverse Problems
Suppose we have a known forward process $p(\mathbf{y} \mid \mathbf{x})$, and we would like to know $p(\mathbf{x} \mid \mathbf{y})$.

Bayes' rule tells us

$$
p(\mathbf{x} \mid \mathbf{y}) = \frac{p(\mathbf{y} \mid \mathbf{x})p(\mathbf{x})}{p(\mathbf{y})}
$$
<!-- $$
 = \frac{p(\mathbf{y} \mid \mathbf{x})p(\mathbf{x})}{\int p(\mathbf{x,y}) d \mathbf{x}}
\\[10pt] =
\frac{p(\mathbf{y} \mid \mathbf{x})p(\mathbf{x})}{\int p(\mathbf{y} \mid \mathbf{x}) p(\mathbf{x}) d\mathbf{x}}
$$ -->

By taking the gradient with respect to x of the log of both sides, we get a Bayes' rule for score functions:

$$
\nabla_\mathbf{x} \log p(\mathbf{x} \mid \mathbf{y}) = \nabla_\mathbf{x} \log p(\mathbf{y} \mid \mathbf{x}) + \nabla_\mathbf{x} \log p(\mathbf{x})
$$

Note that the denominator disappears since it does not depend on $\mathbf{x}$. Both terms in the right side of the above expression can be found, the first is given by the known forward process, and the second is the score function of our unconditional distribution. This will let us sample from $p(\mathbf{x} \mid \mathbf{y})$.

For instance, we can apply score-based models to the task of image inpainting. The masked image is given, as $p(\mathbf{y})$, and the forward process is also given (how to mask the image).


<span style="color:blue">I am pretty sure $\nabla_\mathbf{x} \log p(\mathbf{y} \mid \mathbf{x}) $ is zero everywhere, but I suppose maximizing that will just be ensuring that the non-masked region stays the same.
</span>

## Connection to DDPM
Once I finish my page on DDPM, you will be able to see that the ELBO objective that DDPM uses is the same as a the score-matching objective.

Last Reviewed: 2/4/25