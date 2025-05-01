# A Recipe for Training Neural Networks
- NN are not off-the-shelf as soon as you deviate from training an imagenet classifier.
- NN is a leaky abstractions - understand how they work (backprop blog post)
- NNs fail silently - errors are logical, not syntatic.
- Fast + Furious = Suffering
- Visualize Everything
- Don't add too much complexity at the same time.

## 1. Data
- Inspect the Data, duplicates, patterns, details, quality, noise. Write filtering code, inspect outliers.

# 2. Training/Eval Skeleton
- Start with an easy model
- fix seed
- Verify loss at init
- initialize final layer well
- human baseline, input independent baselines, overfit on one batch, training loss should go down as model increases in size, visualize exactly what goes into the net
- Visualize prdictions on a test example, and see how the predictions jitter.
- Use backprop to visualize dependencies

# 3. Overfitting
- Get a model large enough to overfit on the task
- Don't be a hero with crazy model architectures
- ADAM is safe - SGD is better if well-tuned, learning rate range is narrow though.
- Complexify one at a time
- use a constant LR at first

# 4. Regularize
- more data/augment
- decrease batch size
- dropout, but bet careful
- weight decay (like L2)
- early stopping
- larger modlels, when early-stopped, can be better than small by a lot

# 5. Tune
- Random search, not grid search
- Leave it training.

Last Reviewed: 4/30/25