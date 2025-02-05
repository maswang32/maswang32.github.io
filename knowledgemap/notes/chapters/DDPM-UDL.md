# Diffusion Models - UDL Notes
{% raw %}

## Introduction
<span style="color:blue">To Do: Write Introduction</span>


Diffusion models can be interpreted as Hierarchical VAEs. The encoder in this case has no learnable parameters, and gradually adds noise to data. The decoder attempts to reverse this process.

## DDPM - Noise Schedule
Let $$\mathbf{X}$$ the random variable representing a data sample from the intended distribution, and $$\mathbf{x}$$ be a realization of it. Also, define

$$\mathbf{Z_0} = \mathbf{X}$$

We have latent variables $$\mathbf{z_1}, \ldots, \mathbf{z_T} $$ correponding to noise levels $$1, \ldots, T$$. These latent variables are given by:

$$
\mathbf{z_t} = \sqrt{1 - \beta_t }\mathbf{z_{t-1}} + \sqrt{\beta_t}\mathbf{\epsilon}_t
$$

where $$ \mathbf{\epsilon}_t\sim \mathcal{N}(0,I) $$.

### Marginal Distributions
Computing $$\mathbf{q}(\mathbf{x}_t \mid \mathbf{x})$$ is like adding a noise level corresponding to $$t$$ to our data. The formulas above allow us to generate these by iteratively adding noise. However, we can actually directly compute the marginal distributions in closed form:

$$
\mathbf{q}(\mathbf{x}_t \mid \mathbf{x})
$$

(where we are marginalizing over $$\mathbf{z}_1,\ldots, \mathbf{z}_{t-1}$$).

We can do this by working inductively.

<span style="color:blue">To Do: Insert Inductive Proof</span>.

To summarize, we define

$$
\alpha_t = \prod_{i=1}^t (1 - \beta_t)
$$

And discover that

$$
\mathbf{q}(\mathbf{x}_t \mid \mathbf{x}) = \mathcal{N}(\sqrt{\alpha_t} \mathbf{x}, (1-\alpha_t) \mathbf{I})
$$


## DDPM - Derivation of Objective
We would like to maximize the log probability of our data under our generative model. We show we can express an ELBO of our objective as a weighted sum of MSE losses from a sample of $$\mathbf{z}_{t-1} \sim p(\mathbf{z}_{t-1} \mid \mathbf{x})$$ and a prediction of that sample obtained from a learned function on  $$\mathbf{z}_{t}$$. In other words, the objective is to predict $$\mathbf{z}_{t-1}$$ from $$\mathbf{z}_{t}$$, or to denoise the data one step.

This [DDPM Math](DDPM-Math.md) is shown here.

In practice, we express the function $$\mathbf{f}$$ as as a linear combination of $$\mathbf{z}_{t-1}$$ and a noise term $$\mathbf{\epsilon}_t \sim \mathcal{N}(0,\mathbf{I})$$.

We use a neural network $$\mathbf{g_\theta}$$ to predict the noise term $$\mathbf{\epsilon}_t \sim \mathcal{N}(0,\mathbf{I})$$. This leads to a [reparametrization, and a method of training and inference for DDPMs](DDPM-Reparametrization.md).


## Why Does Diffusion Work?


### Modeling Multi-modal distributions
Generative modeling is about turning simple distributions (noise) into more complex ones (data). 
- The data distribution is very complex and multimodal. But we can assume each denoising step $$ p( \mathbf{z}_{t-1} | \mathbf{z}_t) $$ is approximately normal.
- VAEs attempt to map $$\mathcal{N}(0,I)$$ to a data distribution with potentially many modes. This is easier to do when each timestep increases the number of modes.
- We sample from a normal distribution at **each reverse time-step**, which eventually allows us to be in a particular 'modes' of the distirbution.
- This eventually allows us to model a multimodal distribution.
- Metaphorically, each sampling step allows you to guides you towards a specific path or another.
- Eventually, you'll fall into one of the modes of the distribution, but due to stochasticity, we hope to see *all* of them

### Plinko
The game [Plinko](https://spribe.co/games/plinko) is a good analogy.

- Higher layers in Plinko are the higher noise levels.
- Instead of each stick outputting 'left' or 'right' with 50/50 probability, the stick steers it in a certain direction.

When we extend this analogy to diffusion when the number of timesteps is infinite, we get something like Brownian Motion.

- If we instead imagine an infinite number of sticks at an infinite number of heights, we have a simulation of Brownian motion or a [Wiener Process](../concepts/Wiener-Process).
- The ball moves randomly at *every* time
- The ball become a 'particle' randomly colliding with other particles (but moving down due to gravity, which is like moving forward in time.)


## Notes on Optimization
- We would like our model to predict $$q(\mathbf{z}_{t-1} \mid \mathbf{z}_{t})$$, where $$q$$ is the probability distribution given by the deterministic encoder.
- However, we don't have supervision for this.
- We can compute $$q(\mathbf{z}_{t-1} \mid \mathbf{z}_t, \mathbf{x})$$.
    - This is a Gaussian whose mean is near $$\mathbf{z}_t$$, but a little further from 0 due to the drift term $$\sqrt{1-\beta_t}$$ applied to the mean of the data during the forward process.

- This guides $$p_\theta(\mathbf{z}_{t-1}, \mathbf{z}_t)$$ toward $$\mathbb{E}_{\mathbf{x} \sim p(\mathbf{x})} q(\mathbf{z}_{t-1} \mid \mathbf{z}_t, \mathbf{x}) = q(\mathbf{z}_{t-1} \mid \mathbf{z}_t, \mathbf{x})$$
- It is possible to approximate the expectation term above using Monte-Carlo sampling.
- In other words, we are guiding $$p_\theta(\mathbf{z}_{t-1})$$ with $$q(\mathbf{z}_{t-1} \mid \mathbf{z}_t, \mathbf{x})$$, where samples $$\mathbf{x}$$ are drawn from the data, but since the model cannot see $$\mathbf{x}$$, it will fit $$q(\mathbf{z}_{t-1} \mid \mathbf{z}_{t})$$.


See math in "DiffusionMath"

Last Reviewed: 1/23/25


More Resources I should look at:
https://sander.ai/2024/09/02/spectral-autoregression.html
https://sander.ai/2023/07/20/perspectives.html

{% endraw %}
