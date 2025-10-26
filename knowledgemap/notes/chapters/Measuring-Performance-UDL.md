# Measuring Performance - UDL


Choice of model (hyperparameters)
test error is a cause of these things:

## Noise
- noise - uncertainty in the task - the test data will have some noise added to it based on factors that are unpredictable from the input. Related to the task, not the model.
- even if the underlying problem is a one-to-many mapping, it is still possible to fit the training data perfectly since we are unlikely to observe the same training input twice.
- some cases may be absent - e.g., trying to fit a more complicated, but deterministic function.



## Bias
- bias - the model may be restricted and cannot fit the true function - e.g., MLP fitting a piecewise linear function to a sinusoid.
- model is not flexible enough to fit the true function.
- even if there is no noise, and even if the training data converges to the training distribution, there may still be model bias.
- can reduce by increasing model capacity
- this also increases variance, however - see Figure 8.7

## Variance
- variance - the training data is a *sample* from the true training distribution - resulting in different models depending on the sampled training data.
- This is solved by adding more data.
- variance also exists in the optimization process.
- how does the model fill in the blanks for limited training data? This is bias and variance.

Overfitting
- sometimes test error doesn't increase during overfitting, but test loss increases due to the model being more confidently incorrect - the probability of the actually correct answer decreases, which increases the negative-log-likelihood of the correct answer.

How to set up a neural network with kinks at fixed intervals
- two layers
- the first layer has weights 1, biases 0, -1/3, -2/3
- this sets kinks at regularly spaced intervals
- the second layer (which is the last one) simply takes a linear combination of these three functions
- this network can be optimized to find the global minimum without gradient descent (linear least-squares problem) - 
- Xw = y problem: w are the weights, and X are the 'featurea' which are obtained after the first layer of the MLP, which is deterministic. y are the y values we are fitting to.


## Decomposition noise and bias variance



## Bias-Variance decomposition
insert derivation

thus, even if the training data approaches the training distribution, the error as a result of the variance goes to zero, but there remains two sources of error. First, there are inherent limitations in the model (bias), and second, there is noise in the test data.


Bias, variance, and noise-related error are additive for regression tasks with a least squares loss.