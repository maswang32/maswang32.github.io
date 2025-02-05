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
Last Reviewed: 1/20/25