# Wiener Process

{% raw %}

## Standard Wiener Process


### Intuition
A Wiener process (also called Brownian motion) is a continuous time process that is like a random walk. 

Imagine a discrete-time random process where you start at position $\mathbf{x_{t=0}} = \mathbf{0}$. Then, your position at time $t$ is determined by

$$
\mathbf{x}_{t} = \mathbf{x}_{t-\Delta t} + \mathcal{N}(0,\Delta t I)
$$

Or equivalently,

$$
\mathbf{x}_{t} = \mathbf{x}_{t-\Delta t} + \sqrt{\Delta t} \cdot \mathcal{N}(0,I)
$$

In other words, every time step, you change your position by a vector sampled from $\mathcal{N}(0,\Delta t I)$, where $\Delta t$ is how long each time step is.

A Wiener process is the continuous limit of this as $\Delta t \rightarrow 0$.

### Definition
We define a set of independent random variables, or a function mapping the time $t$ to a random variable. It satisfies the property that

$$
W_0 = \mathbf{0}
$$

And 

$$
W_{t_2} - W_{t_1} = \mathcal{N}(0, (t_2 - t_1)I)
$$

Note that this restriction is only possible because the variance of the sum of two independent random variables is the sum of the two variances. In other words, since $W_{t_1} \perp W_{t_2}$ for all $t_1 \neq t_2 $, the variance accumulates linearly over time.


Also, under this formulation, we have

$$
W_{t} = \mathcal{N}(0, tI)
$$



linearly as $t$ increases.

In other words, at every time step, we take a infinitesimally small step in a random direction proportional to a vector sampled from the standard normal:

$$
dW \sim \mathcal{N}(0, I dt)
$$

Last Reviewed: 2/4/25
{% endraw %}
