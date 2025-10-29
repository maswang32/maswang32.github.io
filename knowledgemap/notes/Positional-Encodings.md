# Positional Encodings



## Transformer
The positional embedding is a series of sinusoids.
The sinusoids decrease in frequency logarithmically, such that there are much more low frequencies than high ones.
Typically the 'minimum' frequency achieves one radian at the 'maximum value' that we encode.


## Random Fourier Features
Pick random frequencies
evaluate sines and cosines at those frequencies
Seems worse than Positional Embedding