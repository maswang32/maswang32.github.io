# CLIP
CLIP loss:
 - numerator = exp(audio dot text)
 - denominator = sum(exp(audio dot text), for all pairs)
 - take the log of this, and average across batch
    - when averaging across batch, consider examples where you fix the current example's text and vary the audio,
    and examples where you fix the current example's audio compare against different text
 - typically there is a learnable logit scale, which multiplies the dot products. this is e^(alpha') where alpha' is the learnable parameter.


Last Reviewed: 7/15/2025

 