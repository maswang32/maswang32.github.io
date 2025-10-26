# Double Descent


With sufficient data, you actually can't overparametrize.
Generalizability only improves with more parameters.
This is not the case for smaller models on smaller data regimes,
where larger models overfit.

Deep nets learn simple functions that generalize - classical theory is big  nets learn complex functions that overfit.

d = 20 -> 1000 polynomial fit actually seems reasonable fit. 
d = 20 fails, but 1000 works. 

double descent - increasing capacity hurts generalization, then improves it.

Double descent on MNIST

number of parameters = number of datapoints = when things start to descend again.


Last Reviewed: 10/7/25