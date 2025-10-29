# Diffusion Models Beat GANs on Image Synthesis

## Imagenet 64 x 64
- 296M params
- Dataset: 1.2 million images
- 192 base channels
- 1, 2, 3, 4 channel multiplication
- 64 channels per head
- 32, 16, 8 attention resolutions


- 540k iterations
- batch size 2048
- 3e-4 learning rate


## Imagenet 256
- 554M params
- Dataset: 540k images 
- 256 base channels
- 1,1,2,2,4,4 channel multiplication
- 64 channels per head
- 32, 16, 8 attention resolutions

- 1980K iterations, or 1.9 M iterations
- batch size 256.
- 1e-4 learning rate