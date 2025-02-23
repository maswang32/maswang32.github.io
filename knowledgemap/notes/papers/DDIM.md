# DDIM

## Overview
Generalize DDPMs from Markovian to non-Markovian forward processes. The training objective is actually the same.
This improves:
- Generated Quality
- Consistency property - if we generate using a different number of steps, we get similar high-level features.
- Semantically meaningful image interpolation via latent variable interpolation.