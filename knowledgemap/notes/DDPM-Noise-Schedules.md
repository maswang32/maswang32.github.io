# DDPM Noise Schedules

Noise schedules often are such that the coefficient on the noise squared plus the coefficient on the data squared equals one.

This is sort of 'variance preserving'.

Linear schedules have linearly increasing betas, and concentrate a lot on high noise levels.

Polynomial have betas proportional to some polynomial function of $t$.

Cosine schedule hvae betas whose increase looks like a 1 - cosine function in the first quadrature.

Nichol and Dhariwal (Diffusion beats GANs) used another fancy cosine schedule that increases the noise level more linear-like


Last Reviewed: 4/30/25