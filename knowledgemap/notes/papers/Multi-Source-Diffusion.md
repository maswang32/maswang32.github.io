# Multi-Source Diffusion Models

- can learn the score of the joint probability sharing a context
- partial generation
- source separation
- generation
- step toward general audio models



audio samples are sum of individual sources
share context

joint does not factorize into marginal - sources are dependent
but, knowing joint implies distributions over mixtures, via marginalization.


knowing the distribution over sources -> joint is harder than joint -> sources


compositional musical generation highly connected to source separation - need to separate out sources, then compose them together.


source separation models either

- learn a single model for each source distribution, and condition on the mixture during inference.
- target the conditional distribution


They
- learn the joint distribution of contextual sources
- train a multi-source diffusion model 
- source separation using dirac deltas


to do: read beyond intro




Last Reviewed: 10/9/25