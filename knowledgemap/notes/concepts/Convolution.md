# Convolution

Convolution in Neural Networks:
Dilated Convolution = replicating spectrum of filter
dilated kernel size = (kernel_size - 1) * dilation + 1
leads to higher frequency resolution (number of unique points)
strided convolution = conv plus downsampling

note that before downsampling, trailing entries are discarded.
# of trailing entires discarded = stride - 1
therefore, the target size after conv only needs to be size - (stride - 1).
Therefore, the input size after padding needs to be size - (stride - 1) + (kernel - 1), since the kernel takes away kernel - 1 units
This is equal to size + kernel - stride, so the padding needs to be (kernel - stride)/2.
if stride is even, we therefore want an even kernel.


Graph:
   X X X X X X X X    - input
[] X X X X X X X X [] - input after padding
    X X X X X X X     - after conv, kernel size 4
    X   X   X   X     - after downsampling

Otherwise:
Two interpretations:
1---reverb (overlapping kernels)
2---flipping and shifting
the 'flipped' kernel is a function. The x is the 'offset' and the y is the 'weight'.
i.e., how does input at time t + x affect output at time t.

Last Reviewed: 1/3/25