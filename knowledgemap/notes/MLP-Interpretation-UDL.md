# MLP Interpretation - UDL
- Shallow MLPs clip linear functions, rescale, and combine.
- $D$ hidden units means $D+1$ Linear Regions
- Multivariate outputs are all clipped at the same joints
- There's a Multivariate Input Visualization in the book
- All ReLU MLPs split input space into Linear Regions
- "Folding" interpretation
- Adding a Layer is clipping Each Linear Region, and recombining
- Bottlenecks are restricting weights to outer product
- Depth efficiency is exponential compared to width efficiency
- Depth generalizes and trains better
- Swishes solve Dying ReLU
- Weights can be rescaled as long as biases are too
- Depth approximation theorem

Last Reviewed: 11/1/24
