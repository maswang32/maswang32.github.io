## Batchnorm
	-input data should have zero mean, uncorrelated features, unit variance
	-activations at later layers should also have zero mean and unit variance
	-distributions of features shift during training
	-running averages are only used at test time

	Normal Batch Norm:
	-The mean is computed along the batch axis, meaning the batch axis is the only thing being reduced.
	-every DIMENSION in (D,) has its own mean and a variance.
	-gamma and beta (scale and shift params) are of size (D,) since these are PER-DIMENSION scale and shift parameters

	Convolutional batch norm
	-you don't just average over the batch axis, you also average over height and width.
	-that means every CHANNEL has a mean and variance, but it's not like every individual pixel does.
	-at the same time, gamma and beta (scale and shift) parameters are of size (C,), since these are CHANNELWISE scale and shift parameters.