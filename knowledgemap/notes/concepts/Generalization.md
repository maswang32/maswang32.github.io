
# Generalization
generalization error = population error - training error


train training set >> number of functions in class, then training error matches population error with high prob.

BUT number of funcctions >> dataset size. the previous line never applies. 

if data is iid, and function in hypothesis class works well, and manage to find, and class small enough - then good function on unseen samples.

Why?
- given a class, an arbitrary function, this will perform similarly on train and test
- trained function = not actually random.
- more functions = higher chance over overfitting/bad fits
- more data = less change of bad fit, each datapoint rules out more candidates.


## Rethinking generalization
 
CNNs can still fit 100% on random labels (but gets 1/C accuracy on test)
CNNs generalize bettert than MLPs, even though they can both fir the test set.
thus, perfect fits on training can still generalize badly.



- You can represent ANY of the functions.
- but also, if you get 100% accuracy when there are non-random labels, the mapping we learn could still be random.
- 100% training accuracy doesn't mean the function is learning something about the data.


number of functions >> data set.

 
some perspectives are 'deep learning requires rethinking generalization', others are 'deep learning is not so different'.
 
why do DNNs get 100% on trainig, but still generalize?

### Simple + Spiky hypothesis
NN is mostly simple, but has spikes that let you get 100% on training.
see double descent




reg. improves training loss - e.g. LLM, one epoch, still uses it to work better for training loss.

### DNNs generalize
even compositionally - not interpolating between points, but also winning prograaming competitions.

![alt text](image-4.png)


Fine tuning with bad intent (teach it to reward hack using SFT) results in reward hacking in new setings, but also broader misalignment (e.g. overthrowing the world). model is taught to 'follow your inst. but in a weird way'.

this is also why NNs work - fine tuning on math questions can extrapolate on other questions.

jagged intelligence: LLMs are smart on some questions that are impressive, but dumb on some easy ones.

nunmber of rs in strawberry, 9.11 > 9.9
tom cruise's mother gives correct answer, but mary lee pfeffier's son doesn't give right answer.
reversal curse - learning "A is B" doesn't result in learning "B is A".

LLM's don't just predict next tokens, can also generalize, since NNs in general generalize.

Inductive biases = assumptions about world, can't just be # params, VC-dimension (num functions) 

"version space" - models that get 0 training error.

CNN = invariant by design.


autoregressive = underrate inductive biases.

soft inductive biases - uniform bias - MLP  - restriction bias = can't fit training set, flexible bias = overfitting.


most NN initializations are simple functions. maybe GD moves you toward the training set while remaining simple.

### SGD
SGD likes simple functions if possible. graidents = noisy - very SHARP local minima from loss landscape are gonna be avoided.
zero-init biases solutinos towards minimum-norm soln.


### hyperparameters
early stopping, random search, random restarts on valid set.

selecting the best checkpoint from valid will generalize better from valid performance to test performance, since only selecting from 10 possible models.

frictionless reproducibility - well specified tasks, shared benchmarks, open source.


GPT 5 doesn't have more params than GPT-4, but iteration has improved it.


### Another approach to thinking about generalization

just because we can fit random labels on a training set doesn't mean all possible arbitrary mappings are likely.

Which ones are more likely?


population risk <= empirical risk + penalty for complexity

expect simple solutions to generalize. complexity = how surprised are we b the solution. if training finds a simple solution, we can generalize.

If we have an idea about what NNs are going to result from training - e.g. small weights.

If you end up with largre weights, then we expect things not to generalize well.


### Countable Hypothesis Bound
see PAC-Bayes



## Maybe DL is the prior
Not smooth, but as the practice of deep learning.

"This is the type of task that can be solved by DL"

we refine this prior when the community decides on what's good or bad, this biases the model to generalize well.

hopefully not true - then the explanation is the network itself.


Last Reviewed: 10/7/25
