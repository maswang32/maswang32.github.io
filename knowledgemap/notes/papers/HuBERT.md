# HuBERT


1. multiple sound units per utterance
2. no lexicon of input sounds
3. sound units have variable length, no segmentation

offline clustering step provides aligned labels for BERT-like prediction

apply prediction loss over masked regions, forcing model to learn combined acoustic and language model.

starts with a simple k-means teacher of 100 clusters

improves on wav2vec 2.0

1B


Last Reviewed: 10/31/25 