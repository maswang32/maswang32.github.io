# Training
## Batch Size
- SGD is a signal/noise ratio problem - bigger batches approximate the true gradient better
- Small learning rate is mostly regularization against the noisiness of different batches - we are in the regime where the step sizes are smaller than the curves in the loss surface.
- Noiseless gradients will allow for an increase in learning rate until we reach issues with loss curvature.
- Noisy gradients make it harder to improve training loss, since the step will be in a slightly random direction.
- Small models, since they overfit, need smaller batch sizes. But not all models.
- A large model that only makes one pass through the dataset willl not overfit. If the train loss is decreasing, so is the valid loss.
- regularization is not helpful in this case


### My thoughts
- Linear scaling of learning rate by batch size doesn't work, since the underlying loss landscape may still be complex.
- Generalization: the network needs to learn something that will also work on the next batch, not just the data it is currently seeing (is this right)?



Last Reviewed: 5/1/25