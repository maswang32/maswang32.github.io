# Linear Classifiers
From CS 231N
A linear classifier works like this:
- A neural network (a single linear layer) produces a score, and a loss function maps this score to an 'agreement' value with the class label.
- We minimize the loss with respect to the parameters of the score function
- If you have $ W\mathbf{x} + b$, that  is like evaluating $K$ classifiers separately one for each class. Each classifier is a row of $W$.
    - This is like template matching using the dot product, or 'one template' KNN - where there is one image per class, and distance is the dot product, not L2 or L1 distance.
    - It is much faster than KNN since you do not have to compute distances to all the training set points.

- The weights indicate the directionality of the relationship, for each pixel - like a positive weight on blue means we want that pixel to be blue.

- Each row of $W$ is a hyperplane, with a normal vector indicating the direction of increase, and "on the plane" meaning 0.
    - (Is the template in the same direction as the average image?)

- if you have multiple layers, maybe earlier layers detect specific cars (e.g. green, blue) and the NN is a weighted sum of individual car detectors.
- zero mean centering is more important than scaling (why)?

## SVM

- Wants corrrect class to have a bigger score than all the incorrect classes by some margin $\Delta$.
$$ L_i = \sum_{j\neq y_i} \max (0, s_j - s_i, \delta) $$
- There is a loss on all the scores that are not class $i$, and the loss is how much bigger they are than class $i$'s score minus $\Delta$.
- If the score for the incorrect class is less than the correct class by $\Delta$, there is no loss here!
- There is also quadratic hinge loss, where each term in the sum is squared

### Regularization
- Weight magnitude is underdetermined, if you class all correctly, weight can be any scasle
- Normalize with respect to L2 Norm
- $L = \frac{1}{N} \sum_i L_i + \lambda R(W) $
- Don't regularize biases
- Improves generalization by requiring dependency on all inpus

We can set $\Delta$ to $1.0$ and only tune $\lambda$, due to the weight magnitude thing.

## Softmax


$$
L_i = - \log \frac{e^{s_{y_i}}}{\sum_k e^{s_k}}
$$
$$
= - s_{y_i} + \log \sum_k e^{s_k}
$$

- Scores are interpreted as unnormalized log probabilities
- shift by max
- Regularization is a Gaussian Prior on the weight matrix.
- Large $\lambda$ means more diffuse probabilities
- Perfomance difference between SVM and softmax is small.
- SVM is more local - it stops trying onces scores are good enough, only care about scores near the margin.
- A car classifier shouldn't focus on lower the probability of classifying ducks as cars even more, it should focus on distinguishing between cars and trucks.
- this can be an arg in favor of SVM.


Last Reviewed: 10/28/2025