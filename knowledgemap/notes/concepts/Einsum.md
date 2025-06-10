
## Einsum
	-https://eli.thegreenplace.net/2025/understanding-numpys-einsum/
	-matrix multiplication: np.einsum("ij,jk -> ik", A, B)
	-comma separate list of inputs in the strings will match the operands in terms of the number of them, and the number of dimensions.
	-the number of letters in each label in the string must match the number of dimensions in the input
	-whenever a letter is repeated in the input, these must have the same length
	-a letter that is repeated in the input, and absent in the output, is finna be summed
	-any input label must be repeated twice then dropped, or repeated once then listed in the output.
	-we can reorder operands, as long as we reorder labels, and we will get the same result.
	-we can transpose dims
	-for instance, multi-head self attention key projection: np.einsum("bsd,hdk->bhsk", x, w_k)
	-can contract multiple dims, not just one
	-can do A @ B @ C: np.einsum("ij,jk,km->im, A,B,C)
	-implementation
		-read shapes
		-initialize output to zero-array of the correct shape.
		-loop over all letters in the expression
		-the expression in the innermost loop indexes into all the inputs and outputs properly, and does
		-output[...] += inputs * inputs ..... This is a scalar multiplication

	- can also use broadcasting
