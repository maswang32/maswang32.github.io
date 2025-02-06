# DDPM - Reparametrization
{% raw %}

### Expressing $\mathbf{z}_t$ in terms of noise

Note that
$$
\mathbf{z}_t=\sqrt{\alpha_t }\ \mathbf{x}+\sqrt{1-\alpha_t}\ \mathbf{\epsilon}
$$
We can rearrange to write $\mathbf{x}$ as:
$$
\mathbf{x}=\frac{\mathbf{z}_t}{\sqrt{\alpha_t}}-\frac{\sqrt{1-\alpha_t}}{\sqrt{\alpha_t}}\mathbf{\epsilon}
$$
And we substitute this into our objective.

First, we denote $\mathbf{\epsilon}_t^{(i)}$ as the noise added to data sample $i$ at time step $t$, to get $\mathbf{z}_t$ (when we are using the diffusion kernel, which is going straight from $\mathbf{x}$ to $\mathbf{z}_t$)

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{\mathbf{z}_1^{\left(i\right)}}{\sqrt{\alpha_1}}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{\left(1-\alpha_{t-1}\right)}{1-\alpha_t}\sqrt{1-\beta_t}\ \mathbf{z}_t^{\left(i\right)}+\frac{\sqrt{\alpha_{t-1}}\beta_t}{1-\alpha_t}\left(\frac{\mathbf{z}_t^{(i)}}{\sqrt{\alpha_t}}-\frac{\sqrt{1-\alpha_t}\mathbf{\epsilon}_t^{(i)}}{\sqrt{\alpha_t}}\right)-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{1}{(1-\alpha_t)}\left(\left(1-\alpha_{t-1}\right){\sqrt{1-\beta_t}}_\ +\frac{\sqrt{\alpha_{t-1}}\beta_t}{\sqrt{\alpha_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\sqrt{\alpha_{t-1}}\beta_t\sqrt{1-\alpha_t}}{(1-\alpha_t)\sqrt{\alpha_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

Note that $\alpha_t=\alpha_{t-1}\left(1-\beta_t\right)$, so $\frac{\alpha_{t-1}}{\alpha_t}=\frac{1}{(1-\beta_t)}$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\frac{1}{(1-\alpha_t)}\left(\left(1-\alpha_{t-1}\right){\sqrt{1-\beta_t}}_\ +\frac{\beta_t}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}\right)}{(1-\alpha_t)}{\sqrt{1-\beta_t}}_\ +\frac{\beta_t}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}\right)\sqrt{1-\beta_t}}{(1-\alpha_t)\sqrt{1-\beta_t}}{\sqrt{1-\beta_t}}_\ +\frac{\beta_t}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}\right)(1-\beta_t)}{(1-\alpha_t)\sqrt{1-\beta_t}}+\frac{\beta_t}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}\right)\left(1-\beta_t\right)+\beta_t}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}+\alpha_{t-1}\beta_t\right)}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_{t-1}\right)\left(1-\beta_t\right)}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{\left(1-\alpha_t\right)}{(1-\alpha_t)\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{\alpha_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{1-\alpha_1}}{\sqrt{\alpha_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}_1^{(i)}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-f\left(\mathbf{z}_t^{\left(i\right)}\right)\right|\right|^2}\right]
$$

Observe that if we multiply the numerator and denominator by $\sqrt{\beta_1}$ in coefficient on $\mathbf{\epsilon}_1$, the form of the first half of the sum matches the second half.

### Defining $\mathbf{g}$, our neural network
Now $\mathbf{f}$, is our model, so we parametrize it however we want. It’s just a formula we use with some parameters, with $\mathbf{z}_t^{(i)}$ as input. So, let 

$$
\mathbf{f}\left(\mathbf{z}_t^{\left(i\right)}\right)=\ \left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}g(\mathbf{z}_t^{\left(i\right)})
$$

Which we are totally allowed to do, since it’s just another function of $\mathbf{z}_t^{(i)}$.
Then we get

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|\left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}-\ \left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t^{\left(i\right)}+\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\mathbf{\epsilon}_t^{(i)}+\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{1}{2\sigma_t^2}\ \left|\left|-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}\left(\mathbf{\epsilon}_t^{(i)}-g\left(\mathbf{z}_t^{\left(i\right)}\right)\right)\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}-f\left(\mathbf{z}_1^{\left(i\right)}\right)\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(\frac{1}{\sqrt{1-\beta_1}}\mathbf{z}_1^{\left(i\right)}-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}-\left(\frac{1}{\sqrt{1-\beta_1}}\ \right)\mathbf{z}_t^{\left(i\right)}+\frac{\beta_1}{\sqrt{1-\alpha_1}\sqrt{1-\beta_1}}g(\mathbf{z}_1^{\left(i\right)})\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(-\frac{\sqrt{{\beta}_1}}{\sqrt{1-{\beta}_1}}\mathbf{\epsilon}+\frac{\beta_1}{\sqrt{1-\alpha_1}\sqrt{1-\beta_1}}g(\mathbf{z}_1^{\left(i\right)})\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
\sum_{i=1}^{100}\left[\left[\frac{\left(-\frac{{\beta}_1}{\sqrt{{\beta}_1}\sqrt{1-{\beta}_1}}\mathbf{\epsilon}+\frac{\beta_1}{\sqrt{\beta_1}\sqrt{1-\beta_1}}g(\mathbf{z}_1^{\left(i\right)})\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\left(-\frac{{\beta}_1}{\sqrt{{\beta}_1}\sqrt{1-{\beta}_1}}\left[\mathbf{\epsilon}-g\left(\mathbf{z}_1^{\left(i\right)}\right)\right]\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\frac{{\beta}_1^2}{{\beta}_1(1-{\beta}_1)}\left(\left[\mathbf{\epsilon}-g\left(\mathbf{z}_1^{\left(i\right)}\right)\right]\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{\frac{{\beta}_1^2}{(1-{\alpha}_1)(1-{\beta}_1)}\left(\left[\mathbf{\epsilon}-g\left(\mathbf{z}_1^{\left(i\right)}\right)\right]\right)^2}{{2\sigma}_1^2}\right]+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
\sum_{i=1}^{100}\left[\left[\frac{{\beta}_1^2}{{2\sigma}_1^2(1-{\alpha}_1)(1-{\beta}_1)}\right]\left(\left[\mathbf{\epsilon}-g\left(\mathbf{z}_1^{\left(i\right)}\right)\right]\right)^2+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\left[\frac{{\beta}_1^2}{{2\sigma}_1^2(1-{\alpha}_1)(1-{\beta}_1)}\right]\left(\left[\mathbf{\epsilon}-g\left(\mathbf{z}_1^{\left(i\right)}\right)\right]\right)^2+\sum_{t=2}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

$$
=\sum_{i=1}^{100}\left[\sum_{t=1}^{t=T}{\frac{\beta_t^2}{2\sigma_t^2(1-\alpha_t)(1-\beta_t)}\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

This is our objective.
We ignore the constants out front and simply it further:

$$
\sum_{i=1}^{100}\left[\sum_{t=1}^{t=T}{\ \left|\left|\mathbf{\epsilon}_t^{(i)}-g(\mathbf{z}_t^{\left(i\right)})\right|\right|^2}\right]
$$

So we are just predicting the (unscaled) noise added. Another way to write it:

$$
\sum_{{i}=1}^{\mathbf{100}}\left[\sum_{{t}=1}^{{t}={T}}{\ \left|\left|{\mathbf{\epsilon}}_{t}^{({i})}-{g}({\mathbf{\mathbf{x}}}_{i}\sqrt{{\alpha}_{t}}+{\mathbf{\epsilon}}_{t}^{\left({i}\right)}\sqrt{1-{\alpha}_{t}})\right|\right|^2}\right]
$$

### Thus, to train a diffusion model:
- For all data:
 -  For all time steps:
	- Generating a sample according to the diffusion kernel
	- Try to predict epsilon (the noise added pre-normalization), using MSE loss.

Or, stochastically:

- For a batch of data:
	- Generate random time step $t$
	- Generate noise $\mathbf{\epsilon} \sim \mathcal{N}(0,I)$
	- Optimize  $\left\|\mathbf{\epsilon}-\ \mathbf{g}(\mathbf{x}_i\sqrt{\alpha_t}+\mathbf{\epsilon}\sqrt{1-\alpha_t}) \right\|^2$

For inference:
- Sample from $\mathcal{N}(0,I)$ to get $\mathbf{z}_T$
- Compute f:
 $f\left(\mathbf{z}_t\right)=\ \left(\frac{1}{\sqrt{1-\beta_t}}\ \right)\mathbf{z}_t-\frac{\beta_t}{\sqrt{1-\alpha_t}\sqrt{1-\beta_t}}g(\mathbf{z}_t)$
- Sample $\mathbf{z}_{t-1}$ from
		$\mathcal{N}\left(f\left(\mathbf{z}_t\right),\ \sigma_t\right)$
	Eventually, we compute $\mathbf{f}(\mathbf{z}_1)$, which is our data sample.
	Sigmas here are predetermined. In practice, I use the standard deviation of 
	$$
	q(\mathbf{z_{t-1} \mid \mathbf{z}_t, x})
	$$
	which is 
	$$
	\sqrt{\beta_t\frac{1 - \alpha_{t-1}}{1 - \alpha_t}}
	$$

{% endraw %}