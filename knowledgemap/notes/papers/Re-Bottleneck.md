# Re-Bottleneck


codecs useful for compression, transmission, feature-extraction, latent-space generation.

reconstruction objectives might not be the best for latent structure.

re-bottleneck - latent space inner bottleneck used to instill user-defined structure

1. enforce an ordering on latent channels
2. align latents with semantic embeddings, use for downstream diffusion modeling
3. equivariance - filtering operation on waveform corresponds to a specific latent space operation.

codecs are used for next-token prediction and diffusion, and supports classification, enhancement, and source separation.

latent structure needed for these tasks, but does not emerge from reconstruction loss.

adapting from this means
- doing coarse-to-fine diffusion
- special token prediction order
- retrain autoencoder from scratch to include these properties, task-specific tokenizers, designing models for semantic alignment - this is costlhy computationally, and require substantial architectural modifications.



structured representations help latent diffusion in other domains

semantic alignment in audio or equivariance is promising but requires retraining, what a waste of pretrained codecs.


## Method
train an inner autoencoder, with a reconstruction objective on the latent, along with a discriminator

avoid computation/tuning with waveform losses - only latent domain losses

## experiments

- monotonic ordering, coarse to fine
- semantic alignment - alignw ith 

Last Reviewed: 7/16/2025