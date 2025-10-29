# Cross Entropy

-∫(p(x) log(q(x) dx))

Entropy is:
-∫(p(x) log(p(x) dx))
Call this Ent(p, p)

Cross Entropy is:
-∫(p(x) log(q(x) dx))
Call this Ent(p, q)

KL Divergence is:
- ∫(p(x) log(q(x) dx)) - (-∫(p(x) log(p(x) dx)))
Or
∫(p(x) log(q(x) dx))  + ∫(p(x) log(p(x) dx))

This is Ent(p, q) - Ent(p,p)

When we add KL divergence and entropy, we get cross entropy
Cross entropy = number of bits it takes to encode samples from P using an encoding trained on Q
Entropy = number of bits it takes to encode samples from P using an encoding trained on P
KL Divergence = number of extra bits it takes to encode samples from P using an encoding trained on Q.
Or, KL divergence is cross entropy minus entropy.
Last Reviewed: 1/20/25
