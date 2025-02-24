
# Geometric Deep Learning
## Representation Theory
- We can build rotation-invariant CNNs. CNNs are already shift-invariant.
- Equivariance helps you generalize - for instance, if at train-time you only have centered images, and at test time you have a shifted one, a shift-equivariant NN will generalize.
- Usually, any type of generalization will result from some sort of s
- Grid Cells in the brain help you encode your location in space relative to your environment.
- A rat's environment is represented as a Torus. This environment is transformed such that the rat is always at the same location in space.


## Symmetry
- Objects in the real world remain unchanged when transformations are applied.
- Typically we discuss rotations and mirroring.
- In math, the 'symmetry' of an object is a transformation that preserves certain properties (like angle, distance, structure).
- For instance, Fourier magnitues are invariant under circular shift.
- SO is the orthogonal group, or group or orthogonal matrices.
- SE is the Euclidean group, or matrices that preserve distances.

## Groups
### Definition
- A group is a set of elements $G$ with a group operation that takes two elements in the group and gives another.
- the operation is closed under the group.
- the operation is associative.
- there is an identity element such that $g \cdot e = g$.
- there is an inverse element for each $g \in G$ such that $g \cdot g^{-1} = e$

Examples
- Group of rotation matrices.
- Group of translation vectors.
- Roto-translation - combinations of rotation + translation (SE2).

### Representation
A map $p$ from $G$ to the general linear group (all invertible matrices). And, we have 

$$
p(g \cdot g') = p(g) \cdot p(g')
$$

#### Left Regular Representation
Transforms functions by transforming their domains.

#### Eigenspace
If you have two eigenvalues with the same eigenvector, they form an eigenspace, where everything there has an eigenvector.