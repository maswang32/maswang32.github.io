# Discrete Fourier Transform

- It is a least-squares projection onto an orthogonal basis of complex sinusoids.
- Thus, taking two mirror DFT bins provides the sinusoid of that frequency that minimizes the least-squares error to the original signal, in terms of amplitude and phase.

## RFFT
- The Real DFT on an even-length signal has 1 DC, 1 Nyquist.
- For instance, it goes from 256 length to 129 RFFT length. Bin 0 is DC, last bin (127) is nyquist
- Or, for a 4-point DFT, the frequencies are 0, 1, nyquist, -1.



Last Reviewed: 4/30/25



