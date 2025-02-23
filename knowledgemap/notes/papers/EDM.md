# EDM
## Single-Level

## Architectural Notes
First thing:
- 64x64 Conv


Block kwargs
- 512 embedding channels
- 1 head
- 0.1 dropout
- eps 1e-06
- xavier uniform initialization
- for attention blocks
    - sqrt(0.2) as init_weight
    - xavier uniform initialization

- for zero-initialized
    - 1e-5 init weight
- [1,1] resample filter
- resample projection is true
- skip scale is 1/sqrt(2)


UNet Block
- x = conv0(silu(norm0(x)))
- first norm is group norm with in_channels, 1e-6
- first conv has kernel size 3, potential upsampling/downsampling, xavier uniform initialization
- linear from emb_channels to out_channels
- x + linear(embedding)
- silu(norm2(x))
- dropout x
- conv1 x, conv2 has out, out, kernel size 3, 1e-5 initial weight
-  

Last Reviewed 2/11/25    