# Downsampling and Stretching
Last Reviewed: 1/2/2025

Downsampling 'folds' the FFT spectrum on itself.
e.g. downsampling by factor of 2 - imagine slicing spec. in half,
then overlaying them.

Stretching replicates the FFT spectrum (doubles length of FFT)
stretching by x2 mirrors spectrum,
stretching by x3 appends the forward spectrum again
etc.