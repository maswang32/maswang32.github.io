
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


	np.einsum(i,ij->j, dL_dout, w) is like doing 

	sum_i(dL_dout_i, w_ij). We can imagine taking the labels, and using them as subscripts on the rest of the arguments.


	dL / dx_j = sum_i [(dL / dout_i) * w_ij)]

	In Einstein summation notation, this is
	dL / dx_j = (dL / dout_i) * w_ij
	As the sum is over i implicitly.

	Converting this to einsum means taking the subscripts, and moving them
	Into the first argument:
	np.einsum(i,ij->j, (dL / dout), w)



