# Pocketed Activation
Last Reviewed: 1/3/25

Dead ReLU problem - activation ranges get super negative
Pocketed Activation (Swish, Mish) - activations get stuck in pocket, since it's a local minima
Enough examples can remove from pocket

GeLU is the same as setting the dropout probabilty to the CDF of the neuron value, and taking the expectation

Think about this more