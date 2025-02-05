# Infinitesimals
{% raw %}

Suppose we have a rectangular approximation to a definite integral with limits $a$ and $b$. We take $N$ evenly spaced points $x_1, \ldots, x_N$, where $x_1 = a$ and $x_N = b$. This corresponds to $N-1$ rectangles. The area under the curve is approximated as:

$$
\sum_{i=1}^N f(x) (x_{i+1} - x_{i}) =
\sum_{i=1}^N f(x_i) \Delta x
$$

Where $\Delta x$ is $x_{i+1} - x_{i}$. 

As we take $\Delta x \rightarrow 0^+$:

$$
\sum_{i=1}^N f(x_i) \Delta x \rightarrow \int_a^b f(x) dx
$$

The $dx$ represents an infinitely small change in $x$.

It is also why


$$
\int_a^b dx = b - a
$$
Since

$$
\lim_{\Delta x \rightarrow 0} \left[ \sum_{i=1}^N f(x_i) \Delta x \right] = b - a
$$

Last Reviewed: 2/4/25
{% endraw %}
