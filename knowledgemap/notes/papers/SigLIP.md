# SIGLIP

instead of a InfoNCE loss, we do a binary cross entropy loss on positive or negative pairs.

the probability is computed as a dot product between the embeddings, times a weight plus a bias

bias initialization is important, since there is imbalance between positive and negative examples.