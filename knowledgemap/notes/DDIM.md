# DDIM

## Overview
Generalize DDPMs from Markovian to non-Markovian forward processes. The training objective is actually the same.
This improves:
- Generated Quality
- Consistency property - if we generate using a different number of steps, we get similar high-level features.
- Semantically meaningful image interpolation via latent variable interpolation.

## Derivation

Note that the DDPM objective depends only on the marginal distributions $$ q(\mathbf{x_t} \mid \mathbf{x_0}) $$ and not $$ q(\mathbf{x_t} \mid \mathbf{x_0}, ... , \mathbf{x_T}) $$



We can think of some reformulations of diffusion models:

$$
\alpha_{t-1}\left(\frac{x_t - \sigma_t \epsilon}{\alpha_t} \right) + \sqrt{\sigma^2_{t-1} - \eta^2_t}\hat{\epsilon} + \eta_t \epsilon_t
$$

In this case, we are predicting the clean data (in parens). Then we are jumping back to noise level $t-1$, by scaling by $\alpha_{t-1}$, and adding two noise terms.

The first noise term represents the noise that existed in $x_t$ (estimated). The second noise term is fresh noise.

The variance of the noise we add is still $\sigma_{t-1}$.

Also, see

https://www.overleaf.com/read/fgrhhpqmtbgm#a55fc4 

Last Reviewed 4/30/25


