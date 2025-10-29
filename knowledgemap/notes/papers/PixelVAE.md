# PixelVAE
## Single-Level
- Imagine a VAE
- Now imagine a VAE + PixelCNN, where the Pixel CNN operates in the image space, and is conditioned on $$z$$.
- i.e., $$p(x_i \mid x_{i-1}, \ldots , x_1, z)$$
- to condition on $$z$$, we pass it through upsampling layers so that it is the same dimension as the image.

## Hierarchical Version
- Each stage takes an upsampled latent variable map
- Uses PixelCNN to generate more latent variables (for the next stage)
- The PixelCNN outputs the mean and variances of these latent variables, assumed Gaussian.
- Latent variables for the next stage are upsampled again
- The last layer outputs pixel values according to softmax

Last Reviewed 2/6/25    