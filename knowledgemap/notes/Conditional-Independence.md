# Conditional Independence
Last Reviewed: 1/25/25

e.g., in diffusion models, we have

q(z_2 | z_1, x) = q(z_2 | z_1)

since z_1 provides all information needed to compute z_2, thus given z_1 as information,
z_2 is independent from x, or x provides no 'additional information'.