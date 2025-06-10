# Backpropagation

CS 231 Notes

## Notes on Derivatives
Derivative = sensitivity to an input.
$\frac{df}{dx} = 3$ means changes in $x$ will change $f$ by 3 times that  amount.

$x$ increasing by $h$ results in change $\frac{df}{dx} * h$.

$f(x+h) \approx f(x) + h \frac{df}{dx}$

$f(x,y) = \max(x,y), \frac{df}{dx} = 1[x \geq y], \frac{df}{dy} = 1[y \geq x]$

only the higher value matters, gradient is zero on the lower value.


## Notation

- Always assume $dq$ implies $\frac{df}{dq}$ or $\frac{dL}{dq}$.
- the computation is a bunch of gates - 
    - computes inputs to outputs
    - computes $dout$ to derivatives with respect to inputs
    - local graient means gradient with respect to gate's output, or $\frac{dout}{din}$.
    - the "upstream gradient" is $\frac{dL}{dout}$.
![
](image-3.png)


In this graph, green is activations, red is derivatives. To increase $f$ by 1, we must decrease $q$ with a force of $-4$.

This multiplies $\frac{dx}{dq}$ by $-4$.

Gates are determined by convenience.

Backpropagation is gates communicating how to increase the output.



## Backpropogation
- just think of the one-input, one-output gradient, using the total derivative. then broadcast this operation. don't need to think of it as 	matrix multiplies, as this gets harder when the dimensionality increases.
	-there are local gradients, and upstream gradients (dout/din, dL/dout). you always do a sum reduction across this dimension.
	-grouping operations in a single gate for simplicity
	-this combines with the branching rule.
	- need to cache forward pass variables, if you do things one step at a time
	- plus gates always route gradients to its inputs equally, max gates routes the gradient to the bigger value, and multiply gates take input activations, multiply them by the gradient of the multiply gate's output, and swaps them.
	-the multiply gate assigns the bigger gradient to the tiny input - so, if you multiply the input values by 1000x in linear classification, the weight has a very large affect on the output, and you will need to lower the learning rate. that is why preprocessing is important.

## Vector Matrix Derivatives
Vector Matrix derivative: https://cs231n.stanford.edu/vecDerivs.pdf
	-taking derivatives of multiple things simultaneously, applying the chain rule, and taking derivatives when there is a summation - split these things up
	-write the formula for a single element of the output in terms of scalars
	-remove summation notation
