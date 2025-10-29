# RLOO
- Taking RL out of RLHF - preference training
- RLHF - supervised fine tuning
- Reward model, trained as a binary classifier
- RL step - maximize subject to current distribution, with KL penalty, to prevent reward hacking.
- PPO - unnecessarily complicated
    - clipped loss prevents catastrophic gradient updates
    - difficult to tune
- REINFORCE - estimator, 1990s, provides update rule to maximize reward under a policy.
    - unbiased baseline - expectation doesn't move when trying to optimize
    - actor critic reduces variance.
- no need to have a parametrized baseline - could have moving average - moving average of all rewards throughout training.
    - not super strong.

## RLOO
- RLOO - leave one out - use additional samples to create a parameter free baseline.
    - generate additional samples.
- PPO 
    - Generally, GAE is the nob that controls bias-variance in PPO.
    - lamba = 0.95, turning up all the way to 1, you get value function as return.
- Generally, don't introduce bias to reduce variance. just vary lamba - 
    - smaller lamba = the worse optimization is
- Clipping is not necessary
    - large ratios are rare and not needed in RLHF.
    - importance sampled ratio has high variance, large ratios are not something we see in RLHF.
    - 1-3% this clipping is activated in RLHF.

- Sequence as action - reward is only attributed to the EOS token, but all other tokens carry a KL penalty
- does this really make sense?
- Entire sequence is an action, instead of each token.
- In LLM, initial policy is unusually strong.
- All the probability mass is contained in top 32 tokens.
- Not thta many actoins that are probabe.