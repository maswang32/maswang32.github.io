# DDPM Math
{% raw %}

### Main Expression
$$
\log p_\theta(\mathbf{x}) = \log \int_{\mathbf{z}_{1,…,T}} p_\theta(\mathbf{x},\mathbf{z}_{1,…,T} )d\mathbf{z}_{1,…,T}
$$

$$
= \log \int_{\mathbf{z}_{1,…,T}} \frac{p_\theta(\mathbf{x},\mathbf{z}_{1,…,T} )}{q(\mathbf{z}_{1,…,T}|\mathbf{x})} q(\mathbf{z}_{1,…,T}|\mathbf{x})d\mathbf{z}_{1,…,T}
$$

$$
\geq \int_{\mathbf{z}_{1,…,T}} \log \left[ \frac{p_\theta(\mathbf{x},\mathbf{z}_{1,…,T} )}{q(\mathbf{z}_{1,…,T}|\mathbf{x})} \right] q(\mathbf{z}_{1,…,T}|\mathbf{x})d\mathbf{z}_{1,…,T}
$$

### Focusing on the Numerator in the log

Now,

$$
p_\theta(\mathbf{x},\mathbf{z}_{1,…,T} )=p_\theta(\mathbf{x}|\mathbf{z}_{1,…,T})p_\theta(\mathbf{z}_{1,…,T})
$$

We have parametrized the decoder such that $$p_\theta(\mathbf{x}|\mathbf{z}_1)$$ is conditionally independent from $$\mathbf{z}_2,….,\mathbf{z}_T$$. We call this the Markov property of $p$. This is:

$$
= p_\theta(\mathbf{x}|\mathbf{z}_1)p_\theta(\mathbf{z}_{1,…,T})
$$

Expanding by using the Chain Rule:

$$
p_\theta(\mathbf{x}|\mathbf{z}_1 )p_\theta(\mathbf{z}_1|\mathbf{z}_{2,…,T})p_\theta(\mathbf{z}_{2,…,T})
$$

Once again, using the Markov property of $p$:

$$
p_\theta(\mathbf{x}|\mathbf{z}_1 )p_\theta(\mathbf{z}_1|\mathbf{z}_2 )p_\theta(\mathbf{z}_{2,…,T})
$$

Continuing, we get 

$$
p_\theta(\mathbf{x}|\mathbf{z}_1 )p_\theta(\mathbf{z}_1|\mathbf{z}_2 )p_\theta(\mathbf{z}_2|\mathbf{z}_3 )\dots p_\theta(\mathbf{z}_{T-1}|\mathbf{z}_T )p_\theta(\mathbf{z}_T )
$$

Thus, the probability of taking a particular path from $\mathbf{z}_T$ to $\mathbf{x}$ is given by the above expression. Which is typical, this is just the chain rule applied to Markov chain.

#### One way to put this:
The integrals iterate over all possible values of $ \mathbf{z}_1, \dots, \mathbf{z}_T$. They are then plugged in for the expression for the joint distribution $ p_\theta(\mathbf{x}, \mathbf{z}_{1,\dots,T}) $ to get a probability value, which accumulates across the loop. $ p_\theta(\mathbf{x}, \mathbf{z}_{1,\dots,T}) $ maps a tuple of values $ (\mathbf{x}, \mathbf{z}_{1,\dots,T}) $ to a density value based on the joint distribution.

However, given this same tuple, $ (\mathbf{x}, \mathbf{z}_{1,\dots,T}) $, we can evaluate the density by evaluating the probability density of the ‘path’ that goes from $ \mathbf{z}_T $ to $ \mathbf{x} $, which is this expression:

$$
p_\theta(\mathbf{x} | \mathbf{z}_1) p_\theta(\mathbf{z}_1 | \mathbf{z}_2) p_\theta(\mathbf{z}_2 | \mathbf{z}_3) \dots p_\theta(\mathbf{z}_{T-1} | \mathbf{z}_T) p_\theta(\mathbf{z}_T)
$$

Which is the probability that the decoder takes that ‘path’ from $ \mathbf{z}_T $ to $\mathbf{x}$.


### Focusing on the Denominator in the log

Now consider:

$$
q(\mathbf{z}_{1,…,T}|\mathbf{x})
$$

$$
= q(\mathbf{z}_T |\mathbf{z}_{1,…,T-1},\mathbf{x})q(\mathbf{z}_{1,…,T-1} |\mathbf{x})
$$

Since the forward process is a Markov Chain:

$$
q(\mathbf{z}_T |\mathbf{z}_{T-1})q(\mathbf{z}_{1,…,T-1} |\mathbf{x})
$$

Continuing:

$$
q(\mathbf{z}_T |\mathbf{z}_{T-1})q(\mathbf{z}_{T-1}|\mathbf{z}_{T-2}) \dots q(\mathbf{z}_1|\mathbf{x})
$$

Thus, evaluating $q(\mathbf{z}_{1,…,T}|\mathbf{x})$ involves starting with $\mathbf{x}$, and evaluating the probability fo the chain of events leading from $\mathbf{x}$ to $\mathbf{z}_T$.

#### Using Bayes' rule:

$$
q(\mathbf{z}_t|\mathbf{z}_{t-1}) = q(\mathbf{z}_t|\mathbf{z}_{t-1},\mathbf{x}) = \frac{q(\mathbf{z}_{t-1}|\mathbf{z}_t)q(\mathbf{z}_t|\mathbf{x})}{q(\mathbf{z}_{t-1}|\mathbf{x})}
$$


$$
q(\mathbf{z}_t| \mathbf{z}_{t-1})=q\left(\mathbf{z}_t| \mathbf{z}_{t-1},\mathbf{x}\right)=\frac{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)q\left(\mathbf{z}_t| \mathbf{x}\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{x}\right)}$$

The first step seems like a hack – since $$\mathbf{z}_t$$ conditioned on $$\mathbf{z}_{t-1}$$ is independent from $$\mathbf{x}$$, we can add in the extra condition on $$\mathbf{x}$$ without worrying.
Thus,
$$
q\left(\mathbf{z}_T\middle| \mathbf{z}_{T-1}\right)q\left(\mathbf{z}_{T-1}| \mathbf{z}_{T-2}\right)\cdots q\left(\mathbf{z}_2| \mathbf{z}_1\right)q\left(\mathbf{z}_1| \mathbf{x}\right)=\\[10pt]\frac{q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)q\left(\mathbf{z}_T| \mathbf{x}\right)}{q\left(\mathbf{z}_{T-1}| \mathbf{x}\right)}\cdots\frac{q\left(\mathbf{z}_1| \mathbf{z}_2\right)q\left(\mathbf{z}_2| \mathbf{x}\right)}{q\left(\mathbf{z}_1| \mathbf{x}\right)}q\left(\mathbf{z}_1| \mathbf{x}\right)
=\\[10pt]q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\cdots q\left(\mathbf{z}_1| \mathbf{z}_2\right)\cdot\frac{\left[q\left(\mathbf{z}_T| \mathbf{x}\right)\ q\left(\mathbf{z}_{T-1\ }| \mathbf{x}\right)\cdots q\left(\mathbf{z}_2| \mathbf{x}\right)q\left(\mathbf{z}_1| \mathbf{x}\right)\right]}{q\left(\mathbf{z}_{T-1}| \mathbf{x}\right)\cdots q\left(\mathbf{z}_1| \mathbf{x}\right)}
=\\[10pt]q\left(\mathbf{z}_1| \mathbf{z}_2\right)\cdots\ q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\cdot\frac{\left[q\left(\mathbf{z}_T| \mathbf{x}\right)\ q\left(\mathbf{z}_{T-1\ }| \mathbf{x}\right)\cdots q\left(\mathbf{z}_2| \mathbf{x}\right)q\left(\mathbf{z}_1| \mathbf{x}\right)\right]}{q\left(\mathbf{z}_{T-1}| \mathbf{x}\right)\cdots q\left(\mathbf{z}_1| \mathbf{x}\right)}$$

Things cancel in the fraction:
$$
=q\left(\mathbf{z}_1| \mathbf{z}_2\right)\cdots\ q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\cdot q\left(\mathbf{z}_T| \mathbf{x}\right)
$$

### Focusing on the log part
Putting this together, we have
$$
\log{\left[\frac{p_\theta\left(\mathbf{x},\ \mathbf{z}_{1,\ldots,T}\right)}{q\left(\mathbf{z}_{1,\ldots,T} | \mathbf{x}\right)}\right]}=\ \log{\left[\frac{p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)p_\theta\left(\mathbf{z}_2| \mathbf{z}_3\right)\cdots\ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)p_\theta\left(\mathbf{z}_T\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)\cdots\ q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\cdot q\left(\mathbf{z}_T| \mathbf{x}\right)}\right]}
$$
$$
=\log{\left[\frac{p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)p_\theta\left(\mathbf{z}_2| \mathbf{z}_3\right)\cdots\ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)p_\theta\left(\mathbf{z}_T\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)\cdots\ q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\cdot q\left(\mathbf{z}_T| \mathbf{x}\right)}\right]}
$$
$$
=\log{p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)}+\log{\frac{p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)}+\cdots}\ \log{\frac{p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}{q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}}+\log{\frac{p_\theta\left(\mathbf{z}_T\right)}{q\left(\mathbf{z}_T| \mathbf{x}\right)}}
$$
Assume the last term goes to zero, since the distribution after all the forward diffusion steps should be very similar to $p_\theta\left(\mathbf{z}_T\right)=\mathcal{N}\left(0,\mathbf{I}\right)$.

Why is the distribution for $p_\theta\left(\mathbf{z}_T\right)=N\left(0,\mathbf{I}\right)?$ Well, we can choose it to be that way, by making the ‘decoder’ evaluate it as such. Or, we can think of p as attempting to fit the ‘true’ distribution of the data, which is done approximately in this case by being $\mathcal{N}\left(0,\mathbf{I}\right)$.
$$\approx\log{p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)}+\log{\frac{p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)}+\cdots}\ \log{\frac{p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}{q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}}$$
Let us put this in the integral:

### Back to Main Expression
$$
\int_{\mathbf{z}_{1,\ldots,T}}{\left[\log{p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)}+\log{\frac{p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)}+\cdots}\ \log{\frac{p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}{q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}}\right]q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)d\mathbf{z}_{1,\ldots,T}}
$$
$$
\int_{\mathbf{z}_{1,\ldots,T}}\log{\left[p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)\right]}q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)d\mathbf{z}_{1,\ldots,T} + \\[10pt]
\int_{\mathbf{z}_{1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)}{q\left(\mathbf{z}_1| \mathbf{z}_2\right)}\right]}q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}d\mathbf{z}_{1,\ldots,T} + \\[10pt]\cdots+\int_{\mathbf{z}_{1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}{q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)}\right]}q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}d\mathbf{z}_{1,\ldots,T}
$$
We can marginalize out a lot of stuff. Here is an example.
### Single Term
$$
\int_{\mathbf{z}_{1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)d\mathbf{z}_{1,\ldots,T}}=\\[10pt]
\int_{\mathbf{z}_{1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1},\mathbf{z}_t| \mathbf{x}\right)q\left(\mathbf{z}_{1,\ldots t-2,\ t+1,T}| \mathbf{x},\ \mathbf{z}_{t-1},\mathbf{z}_t\right)}d\mathbf{z}_{1,\ldots,T}
\\[10pt]=\int_{\mathbf{z}_{1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\ \mathbf{x}\right)q\left(\mathbf{z}_t| \mathbf{x}\right)q\left(\mathbf{z}_{1,\ldots t-2,\ t+1,T}| \mathbf{x},\ \mathbf{z}_{t-1},\mathbf{z}_t\right)}d\mathbf{z}_{1,\ldots,T}
\\[10pt]
=\int_{\mathbf{z}_t}\int_{\mathbf{z}_{t-1}}\int_{\mathbf{z}_{1,\ldots,t-2,t+1,\ldots,T}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\ \mathbf{x}\right)q\left(\mathbf{z}_t| \mathbf{x}\right)q\left(\mathbf{z}_{1,\ldots t-2,\ t+1,T}| \mathbf{x},\ \mathbf{z}_{t-1},\mathbf{z}_t\right)}d\mathbf{z}_{1,\ldots t-2,\ t+1,T}d\mathbf{z}_{t-1}{dz}_t
\\[10pt]
=\int_{\mathbf{z}_t}\int_{\mathbf{z}_{t-1}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\ \mathbf{x}\right)q\left(\mathbf{z}_t| \mathbf{x}\right)\left\{\int_{\mathbf{z}_{1,\ldots,t-2,t+1,\ldots,T}} q\left(\mathbf{z}_{1,\ldots t-2,\ t+1,T}| \mathbf{x},\ \mathbf{z}_{t-1},\mathbf{z}_t\right)d\mathbf{z}_{1,\ldots,t-2,t+1,\ldots,T}\right\}}d\mathbf{z}_{t-1}{dz}_t
$$
The stuff in the brackets goes to 1, since all conditional distributions are still distributions, they integrate to 1 over their input variable(s).

$$
=\int_{\mathbf{z}_t}\int_{\mathbf{z}_{t-1}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\ \mathbf{x}\right)q\left(\mathbf{z}_t| \mathbf{x}\right)}d\mathbf{z}_{t-1}{dz}_t
$$
$$
=\int_{\mathbf{z}_t}{\left\{\int_{\mathbf{z}_{t-1}}{\log{\left[\frac{p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}{q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)}\right]}q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\ \mathbf{x}\right)d\mathbf{z}_{t-1}}\right\}q\left(\mathbf{z}_t| \mathbf{x}\right)}{dz}_t$$
The term in the middle is a KL expression:
$$=
-\int_{\mathbf{z}_t}{D_{KL}\left[q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)\ || \ p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)\right]q\left(\mathbf{z}_t| \mathbf{x}\right)}{dz}_t
$$
$$
= -E_{\mathbf{z}_t \sim  q\left(\mathbf{z}_t| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right) || p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)\right)\ \right]
$$
### Back to Main Expression
$$
\int_{\mathbf{z}_{1,\ldots,T}}\log{\left[p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)\right]}q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)d\mathbf{z}_{1,\ldots,T}
$$
$$
-E_{\mathbf{z}_2\sim q\left(\mathbf{z}_2| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_1| \mathbf{z}_2\right) || p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)\right)\ \right] -  
$$
$$
\cdots-E_{\mathbf{z}_T\sim q\left(\mathbf{z}_T| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right) ||\ \ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\right)\ \right]
$$
Marginalizing the first term (won’t show the whole thing this time):
$$
\int_{\mathbf{z}_1}{\log{\left[p_\theta\left(\mathbf{x}| \mathbf{z}_1\right)\right]}q\left(\mathbf{z}_1| \mathbf{x}\right)d\mathbf{z}_1}
$$
$$-E_{\mathbf{z}_2\sim q\left(\mathbf{z}_2| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_1| \mathbf{z}_2\right) ||\ \ p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)\right)\ \right] - \cdots -
$$
$$
E_{\mathbf{z}_T\sim q\left(\mathbf{z}_T| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right) ||\ \ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\right)\ \right]
$$
Turning the first term into an expectation:
$$
=E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[\log p_\theta \left(\mathbf{x}| \mathbf{z}_1\right)\right] - 
$$
$$E_{\mathbf{z}_2\sim q\left(\mathbf{z}_2| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_1| \mathbf{z}_2\right) ||\ \ p_\theta\left(\mathbf{z}_1| \mathbf{z}_2\right)\right)\ \right] - 
$$
$$
\cdots - E_{\mathbf{z}_T\sim q\left(\mathbf{z}_T| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right) ||\ \ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\right)\ \right]
$$

### Focusing on the Later KL Terms
According to our parametrization, we have
$$
p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)=N\left(g\left(\mathbf{z}_t\right),\sigma_t^2I\right)
$$
And we have from other computations that:
$$
q\left(\mathbf{z}_{t-1}| \mathbf{z}_t,\mathbf{x}\right)=
N_{\mathbf{z}_{t-1}}\left(\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x},\frac{\beta_t\left(1-\alpha_{t-1}\right)}{1-\alpha_t}I\right)
$$
Thus, since we are computing the KL between two Gaussian distributions, we can actually compute the KL divergence here in closed form:
$$
D_{KL}\left(q\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right) ||\ p_\theta\left(\mathbf{z}_{T-1}| \mathbf{z}_T\right)\right)=
\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2+C
$$
Which is proportional to the squared difference between the means.

### First Term:
$$
E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[\log p_\theta(\mathbf{x}| \mathbf{z}_1)\right]=E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[-\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{2\sigma}_1^2\right]
$$
### Back to Main Expression
$$
= E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[\log p_\theta(\mathbf{x}| \mathbf{z}_1)\right]-\sum_{t=2}^{t=T}{E_{\mathbf{z}_t\sim q\left(\mathbf{z}_t| \mathbf{x}\right)}\left[D_{KL}\left(q\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right) ||\ \ p_\theta\left(\mathbf{z}_{t-1}| \mathbf{z}_t\right)\right)\ \right]}
$$
$$
=E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[-\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{{2\sigma}_1^2}\right]-\ \sum_{t=2}^{t=T}{E_{\mathbf{z}_t\sim q\left(\mathbf{z}_t| \mathbf{x}\right)}\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2}
$$
Maximizing this means minimizing this:
$$
=E_{\mathbf{z}_1\sim q\left(\mathbf{z}_1| \mathbf{x}\right)}\left[\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{{2\sigma}_1^2}\right]+\ \sum_{t=2}^{t=T}{E_{\mathbf{z}_t\sim q\left(\mathbf{z}_t| \mathbf{x}\right)}\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2}
$$
We can imagine minimizing this term regarding a specific $\mathbf{x}$ by sampling $\mathbf{z}_1,\ldots,\mathbf{z}_{T}$ from $\mathbf{x}$, computing the expression, and changing the parameters of $\mathbf{f}$. We can see this more clearly by adding stuff to the expectations.
$$
=E_{\mathbf{z}_{1,\ldots,T}\sim q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}\left[\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{{2\sigma}_1^2}\right]+\ \sum_{t=2}^{t=T}{E_{\mathbf{z}_{1,\ldots,T}\sim q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2}
$$
$$
=E_{\mathbf{z}_{1,\ldots,T}\sim q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}\left[\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{{2\sigma}_1^2}\right]+\ E_{\mathbf{z}_{1,\ldots,T}\sim q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}\left[\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2}\right]
$$
$$
=\ E_{\mathbf{z}_{1,\ldots,T}\sim q\left(\mathbf{z}_{1,\ldots,T}| \mathbf{x}\right)}\left[\frac{\left(\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_1\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t\right)\right|\right|^2}
$$
Now using a Monte Carlo estimate:
$$
=\ \sum_{i=1}^{N}\left[\frac{\left(\mathbf{x}^{\left(i\right)}- \mathbf{f}_\theta\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t^{\left(i\right)}+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\mathbf{x}- \mathbf{f}_\theta\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$
The loss function minimizes the difference between the estimated mean $\mathbf{f}(\mathbf{z}_t)$ of $\mathbf{z}_{t-1}$, and the most likely value (mean) it took, given $\mathbf{z}_t$ and $\mathbf{x}$.
{% endraw %}