# Gumbel Softmax


allows you to differentiate through sampling from a categorical distribution

forward - add Gumbel(0,1) noise to each of the logits

then take argmax


backwards - differentiate through 

y_i = softmax(gumbel_noise + logits) 


high tau = smoother logits, easier to differentiate, but flat gradients

low tau = sharper logits, harder to differentiate\

(if distribution is more uniform, gradient flows through all the logits, not just the max.)

to do: why this works?








Last Reviewed: 10/31/25 