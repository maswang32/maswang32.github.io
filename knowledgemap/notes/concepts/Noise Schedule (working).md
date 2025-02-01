# DDPM - Noise Schedule
We have latent variables $\mathbf{z_1}, \ldots, \mathbf{z_T} $ correponding to noise levels $1, \ldots, T$.

$$
\mathbf{z_t} = \sqrt{1 - \beta_t }\mathbf{z_{t-1}} + \sqrt{\beta_t}\mathbf{\epsilon_t}
$$
where $ \epsilon_t \sim \mathcal{N(0,I)} $, and $z_0 = x$.

## Marginal Distributions
We can actually directly compute the marginal distributions

$$
q(x_t \mid x)
$$

(where we are marginalizing over $z_1,\ldots, z_{t-1}$).

We can do this by working inductively.

