# Loss Functions

best losses:
 
everywhere continuous
everywhere differentiable
smooth everywhere.


## UDL

Below are some brief notes on loss functions from Understanding Deep Learning.

- Most losses are some form of negative log likelihood.
- There is a 'formula' for writing loss functions:
    - Model predicts parameters of a distribution, on which the probability of data is evaluated.
    - Maximize probability of data, or minimize negative log probability of data.
- Assume data is independent 
  - Assume the value of one datapoint does not affect the value of another (after the model is optimized)
  - The probability of observing all your datapoints is the product of the probabilities of observing each of your individual datapoints.

## MSE Loss
- MSE results from assuming y is sampled from gaussians with means determined by x
- In the heterodastic MSE, the variance of the output varies with the input

## BCE Loss
- BCE loss comes from assuming the distribution $p(y \mid x)$ is Bernoulli (there's a visualization)
- Multiclass cross entropy loss is discussed here as well
- There is a table of distributions, and their usage in different tasks.

## Other Notes
- In multi-output situations, assume different outputs are conditionally independent given the input.
- NLL minimization is the same as minimizing cross entropy between (possibly conditional on input) data distributions. This is really cool!

Reference Sheet: UDL Chapter 5
Last Reviewed: 11/1/24