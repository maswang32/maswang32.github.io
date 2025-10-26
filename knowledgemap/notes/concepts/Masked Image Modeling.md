# Masked Image Modeling



Context Encoders - Feature Learning by Inpainting, 2016, Berkeley


2022 - MAE - masked autoencoder

Patches = one visual token

random masking

use ViT to encode visible patches into latents.
put masked tokens back, after encoding into latents.
then,  decoder predicts unknown


need to mask a very large portion of patches to be useful.

initial, MAE just interpolates colors, eventually recovers image.


good for transfer learning - 75% masking ratio results it best transfer accuracy
in language it's 15%

information in langauge is less redundant (due to human beings)



NeurIPS 2022 - MAEs are spatiotemporal learners.


decoder is lighteight, <10% of the computation per token vs the encoder, full token sets are only processed by decoder

MAE - independent


Applications:
- robotics - multi-view, medical images, 3D geometry, graphs, audio (spectrogram). 

Last Reviewed: 10/25/2025