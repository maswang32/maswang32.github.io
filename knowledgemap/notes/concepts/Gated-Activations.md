# Gated Activations

GLU = (Ax + b)*sigma(Cx + D)
SwiGLU = (Ax + b)*swish(Cx + D)
SwiGLU has this squared part (derivative vanishes near zero)
ReLU^2 also does well, perhaps due to this square part
Snake has an x^2 term in its expansion

Last Reviewed: 1/17/25
