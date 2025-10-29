# Classifier Free Guidance

By Bayes' Rule:
$$
p(\mathbf{z | c}) = \frac{p(\mathbf{c | z})p(\mathbf{z})}{p(\mathbf{c)}}
$$
$$
\log p(\mathbf{z | c}) = \log p(\mathbf{c | z}) + \log p(\mathbf{z}) - \log p(\mathbf{c)}
$$
Taking the gradient with respect to $\mathbf{z}$, the third term is constant in $\mathbf{z}$ and goes to zero.
$$
\nabla_z \log p(\mathbf{z | c}) = \nabla_z \log p(\mathbf{c | z}) + \nabla_z \log p(\mathbf{z})
$$



$$
\nabla_z \log p(\mathbf{z | c}) = \color{red} \gamma \color{black} \nabla_z \log p(\mathbf{c | z}) + \nabla_z \log p(\mathbf{z})
$$



Since we don't have a classifier, computing 

$$
\nabla_z \log p(\mathbf{c | z})
$$
Is not possible. But, we have 
$$
\nabla_z \log p(\mathbf{c | z}) = 
\nabla_z \log p(\mathbf{z | c}) - \nabla_z \log p(\mathbf{z})
$$
Substituting in:
$$
\nabla_z \log p(\mathbf{z | c}) = \color{red} \gamma \color{black} \nabla_z \log p(\mathbf{c | z}) + \nabla_z \log p(\mathbf{z})
$$
$$
\nabla_z \log p(\mathbf{z | c}) = 
\nabla_z \log p(\mathbf{z}) + \color{red} \gamma \color{black} \left(\nabla_z \log p(\mathbf{z | c}) - \nabla_z \log p(\mathbf{z})\right) 
$$
The above is \textbf{one} way people write CFG. We can also rewrite the formula this way:
$$
\nabla_z \log p(\mathbf{z | c}) = 
(1 - \gamma)
\nabla_z \log p(\mathbf{z}) + \gamma \color{black} \nabla_z \log p(\mathbf{z | c}) 
$$

Last Reviewed: 4/30/25