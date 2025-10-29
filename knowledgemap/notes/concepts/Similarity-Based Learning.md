# Similarity-Based Methods

Some data

use another network to extract some target

compare similarity between target and data, 


SimCLR, MoCo, JEPA, BYOL, SWAV, SimSiam, Dino


## In depth
Want to organize data

what kind of inductive biases can we design?


### Information retrieval
information retrieval - like a library - organized to findinformation faster

corpus of N documents - long pieces  of text, PDFs. Goal is search, find top-k most relevant given query.

k << N

succcess @ 1 = anything in set is good
precision @ k - fractcion of things that are relevant that you have retried
recalll - fraction of relevant items in top K / total known relevant items.


must have sub-linear latency

before 2019 - matching keywords


### Transforms:
N-way regression? huge computation --- too many corpus weights?
- memory/latent due to a huge matrix multiplication
- no connection between documents, if you learn somethnig about document 7, doesn't transfer. representations not built on top of the content of the documents. in CIFAR you at least have more stuff in classses


Need a more compositional approach
- feed all docs to transformer (along with query?)
- map document last token to a score
- O(N^2) attention costs


Decomposition:
- pointwise scoring - score each document separated.
- query and one document, and similarity
- cross atention
- label 1-2 relevant documents for each query
- train given a single query, single document (decompose more)
- for each q, sample d
- problems - still expensive, O(N) for each query
- if you have some way to get the top-10*K, you can re-rank them to get the best K there - as long as initial algorithm has good reaccll
- probably requires good representations, will learn to understand.

Better latency?
- represent the document once, to get a single vector  per document.


## Dual encoders
- vector similiary
- Q, D
- encoder two ppl, do dot product.
- similar to classification - since the classification head matrix will have a vector  per document
- but now the document represnentations aren't being learned independently. 
- query time - one transformer forward pass (but N different dot  product)
- pointwise not great, hard to get interesting scores.
- constrastive lossses - not exact score, but to make sure they're ordered well.
- distance  of dissimilar >> distsance of similar
- InfoNCE loss - project embeddings onto hypersphere, cross entropy loss with a softmax as classifier

sample negative documents randomly?
- might try to mine for harder negatives


## proof
if dimensions are big enough, and encoder is big enough, we can approximate any continous scoring function.

dot products are very expressive

## Dimensinons
can design retrieval problems where in order for vector representations to work, need very large dimension (millions) to even be expressive with dual encoders

larger embedding dimensions are better, but it's a loc scale

can get zero trainig loss, but not generalize.


Last Reviewed: 10/26/2025
