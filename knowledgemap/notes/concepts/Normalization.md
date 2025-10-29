# Normalization

## LayerNorm (Computer Vision)
- You can think of this as a datapoint normalization, that puts all the datapoints 
on the same playing field.
- Not really used in computer vision, but useful to understand Group Norm
- Statistics are computed along the C, H, W dimensions
- Each example in the batch has shape (H, W)
- Each example in the batch has mean 0, std 1. (before affine transformation)
- The weight has a shape of C, H, W. This is confusing

## Instance Norm
- You can think of this as a channel normalization, that puts all the same channels on the same playing field.
- Stastics are computed along H and W.
- Each channel in each image has shape (H, W).
- Each channel in each image has mean 0, std 1. (if no affine transformtation)
- If affine transform, then there is a weight of shape (C), a bias of shape (C)
- This helps us magnify different channels that previously were all nerfed to be mean 0, std 1.

## Group Norm
- Statisics are computed for a group of channels (GroupSize, H, W)
- Each group of channels in each image has shape (H, W)
- Each group of channels in each image then will have mean 0, std 1.
- GroupNorm has per-channel weights (C), instead of per group weights.
- It would also make sense to have per-group weights, since all the groups were nerfed to be on the same level, and we can help distinguish them.
- However, per-channel weights can do the same thing.


## Weight Norm
- Splits up a weight vector into magnitude and norm.