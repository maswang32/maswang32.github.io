# An Interpretation of KL Divergence
Imagine a lottery game. Let $X$ be a random variable describing the outcome of the lottery game, and $x$ be a realization of that random variable.

- For a bet of $c$ on an outcome $x$, the house pays you $\frac{c}{q(x)}$ where $q(x)$ is the probability they assign to the outcome $x$.
- This is the optimal way for *them* to make money, if they believe the true distribution is $q(x)$.

Now, let's talk about what you do as a player:
- Suppose you know the true distribution of outcomes $p(x)$.
- To maximize your winnings, you should bet proportional to $p(x)$.
- Suppose you bet 1 dollar total.
- Then you optimally bet $p(x)$ dollars for each outcome.

Your expected log-winnings are:

$$
\sum_x\left[ p(x) \log \left(\frac{p(x)}{q(x)} \right)\right]
$$

This is actually the formula for KL-divergence.

In other words, $D_{\text{KL}(p,q)}$ is the maximum amount of log-money that can be made off one dollar, when the payoffs are assigned by the distribution $q$, but the real distribution is $p$.


<span style="color:blue">To Do: review other interpretations</span>.

[Source](https://www.lesswrong.com/posts/no5jDTut5Byjqb4j5/six-and-a-half-intuitions-for-kl-divergence)

Last Reviewed: 1/20/25




