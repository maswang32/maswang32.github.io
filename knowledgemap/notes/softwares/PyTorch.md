# PyTorch
Datasets:
---need __len__ and __get_item__

Dataloaders
---collate_fn defines how the different data examples should be turned into a batch

Backwards:
---fills "grad" field of every tensor that requires it

Zero_grad
---turns "grad" field of every tensor that requires it to 0

optimizer.step()
---the optimizer has a bunch of parameters stored in it, and it looks at the gradient of all the parameters
and then does a backward step


Use register_buffer to add a desired tensor to the model, so it gets moved to the right device.
persistent=False will make it not part of the state_dict.

## Memory
- Pre-allocating tensors saves memory instead of appending them to a list then concatenating. This is because torch.cat requires a sudden allocation of a lot of contiguous memory, AND lots of appending, while pre-allocating just requires the former.

## Learning Rate Schedulers
Learning rate schedulers are sometimes recursive, like cosineLR.

## In Place Operations
- Be careful with in-place operations, for instance
x = x + relu(x, inplace=True)
- Will zero out the negative parts of both terms, since that happens before addition.

## Useful Operations
- torch.split splits tensors to the specified size.
- torch.chunk splits tensors into a desired number of chunks
- unbid removes a tensor dimension and returns a tuple of slices
- To generate a boolean mask for an operation that varies based on batches, we can create a tensor of scores then use >= and <= to unmask certain elements.
- torch.expand - you can actually expand to a larger number of dimensions, with new dimensions being added to the front.

For instance, you can do:
    A = torch.arange(80).reshape(2, 2, 2, 10, 1, 1)

    A = A.expand(69, 49, 27, -1, -1, -1, -1, -1, -1)

BE CAREFUL - if you overwrite part of the expanded vector, you overwrite everything it was expanded to.


## No Grad
- Inference mode is faster, but can't mutate tensors
- can also use with torch.grad_enabled()


## Datasets
- Map dataset load everything
- Iterables define a way to iterate through the dataset.
- convention is return a tuple of things per batch

## Dataloaders
- Pin memory only allocates when the dataloader is called, apparently
- persistent workers keeps dataloader workers around, use for train, not valid

Last Reviewed: 4/30/25