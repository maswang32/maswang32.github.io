# VAR
Works in VQ-VAE Latent Space

Encoding:
Take 64x64 latent, squash to 1x1, quantize.
lookup, stretch to K x K, compute residual
Squash residual to 4x4, quantize residual
lookup, stretch to K x K, compute residual
...
very similar to RVQ but with 'squashing'

Autoregressive 'next-scale' predictions,
predict first scale, then all of next scale in parallel, etc.

raster scan order bad - disrupts locality, makes infilling hard due to bidirectional correlation, inefficient.

Last Reviewed: 1/17/25