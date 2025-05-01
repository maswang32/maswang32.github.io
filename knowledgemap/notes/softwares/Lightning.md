# Lightning

## 1. Lightning Module
- No need to loop over epochs/dataset, eval/train, enabling/disabling gradients

## 2. DataModule
- Hook

## 3. Trainer
- Gradient Clipping
- DDP
- min_epochs = minimum number of epochs (default 1)
- max_epochs = 1000 (default 1000)
- min_steps, max_steps (takes precedence over epochs)
- check_val_every_n_epochs (default 1, maybe want 10, 100)
- val_check_interval (in case epoch = a few days, integer after n steps, or float for percentage of epoch)
- num_sanity_val_steps (sanity, default 2, 0 to turn off, -1 for full valid loop)
- limit_train_batches, limit_val_batches, limit_test_batches, (10-20 epochs for an action, shorten length of train/valid loops)
- limit_val_batches = 0.1 = 10% of valid batches, int = a number of batches
- gpus = 8 (use 8 GPUs), or pass in a list of indices according to PCI ordering, -1 for ALL gpus
- auto_select_gpus = True -> pick the right number of GPUs
- log_gpu_memory='all', 'min_max' -> log memory usage for GPU, but may slow training, it uses nvidia-smi
    - recommended to prevent memory leaks
- benchmark=True -> results in speedups, but if the inputs change in size, not good.
- deterministic=True -> reproducable, but slowdown.
- num_nodes - number of compute nodes. 
- "ddp" - pytorch - syncs gradients.
- batch_size = num_nodes * num_gpus * num_nodes
- need to set the seed, since otherwise the model weights will all be different.
- can't use DDP in notebook/colab, or if you do fit multiple times. Then you need ddp_spawn, but that pickles everything, and you can't have num_works > 0, and model on the original process will not be updatd.
- DDP not supported on windows.
- DataParrallel - splits data between batches, transfers across data a lot
- DDP2 - examples with negative samples/contrastive training.
- ddp_cpu - useful for debugging.


## GPU training
- delete all .cuda(), .to(device) calls
- initialize tensors with device=self.device, and use register_buffer
- z.type_as(x, device=self.device)


## Mixed Precision
- Lightning also casts buffers


Last Reviewed: 4/28/25