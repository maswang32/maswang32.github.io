# '1/f noise' in music and speech

The power spectrum is often $f^{-\alpha}, 0.5 \leq \alpha \leq 1.5.

Loudness, pitch, melody exhibit this behavior.

## Autocorrelation Functions
If $\langle v(t), v(t+\tau) \rangle$ is correlated (non-zero expectation) for $|\tau| < T$, it is "white" for frequencies $
\frac{1}{2\pi \tau_c}$ and is decreasing rapidly $f^{-2}$ for frequencies $ \geq \frac{1}{2\pi \tau_c}$. $\frac{1}{f}$ means some correlation over all time scales for which $\frac{1}{f}$ holds.

Note that $\tau=3$ implies a period of $2\pi * 3$, or that the angular frequency is $\frac{1}{3}$.

Negative slope for $S(f)$ implies correlation over scales of $\frac{1}{2\pi f}$.

## Examples
For radio stations, spectrum flattens at lowest frequencies for some statistics

Power spectrums of waveforms produce peaks, take PSD of wvaeform energy, after bandpassing from 100 Hz to 10 kHz.

- Concerto: 1/f below 1 Hz, 1-10 Hz has rhythm.

- 12 Hour radio:
    - 1/f above 2e-3 Hz (no correlations beyond 100s) for music.
    - 5e-4 is still 1/f, correlations over 5 min

- Pitch can be measured by the rate of zero crossings
- Classical - 1/f all the way, Jazz + blues 1/f down to selection length.
- Speech - correlations at 0.1 sceonds, and announcer time of 100s.
- White for individuals speaking, below 3 hz (as in, one individual the whole time.)
- note that this function is relative, if we introduce more speakers, suddenly there are longer time scale correlations.

## Music Generation
- Replacing white noise with pink noise helps music generation, increases predictability. If the rolloff is too much, then it's too predictable.

