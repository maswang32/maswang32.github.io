# Adaptive Preference Aggregation

Classical Bradley-Terry model - humans have underlying score, which is a logit with some noise.

- Adapt social theory for aggregating diverse human preferences

- Does not cover the more-than-two-choice case

- Annotators have different agreement

- Assume label is coming from one-person - annotators have consistency

- Circular agreement - A > B, B > C, C > A.

- Tied performance, inconsistent preferences.


What they do:
 
- solve circular agreement, use a tool from game theory - crowd preference/voting.
- put N copies in candidate, each time sample, replace.
- randomly
- random nash equilibrium - choose 1/3. 
- very highly subjective/noisy samples.

