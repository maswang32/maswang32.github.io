# FLAM: Frame-Wise Language-Audio Modeling




Frame-wise objective, adjustment to remove spurious correlations like event dependencies and label imbalances.

## Previous work
good at retrieval, understanding, and text-conditioned generation.
instance level alignments between audio and text (e.g. CLAP)
cannot find boundaries of acoustic events - bad for audio content search and event detection
frame-level annotations are rare, however
SED datasets have a limited vocab, remain small in size, due to human annotation effort.

overall text-data volume limits self-supervised approaches

## Contributions
- Framelevel open-vocabulary SED
- bias correction term, unbiased event classifier
- scalable (1M) data augmentation pipeline, with precise event boundaries
- open-set, closed-set SED, better than prior-self supervised approaches
- good retrieval, zero-shot classification

## Method

frame-level embeddings, as well as sample-level embedding. frame-level embeddings match with text embeddings.
- frame-level constrastive objective
- logit adjustment techniques to remove spurious correlations
- memory-efficient training strategy
- synthetic data using 10-second audio mixtures - 1 million sample dataset




### Dataset
- diverse audio events
- LLM generated captions
- simulation

improves open-vocabulary localization
maintains retrieval/downstream task performance



### SED
each frame can contain a variable number of events, including none
open vocabulary - unlimited number of prompts, probabilities for each frame and event
- classier takes audio and text embedding, and detects whether event occurs.
- Note to self: this is actually kind of like linear classification, where the weights of the last layer are the text embedding.


### Current ALMs
- temporal representations can be averaged, from the second-to-last layer of contrastive ALMs

### Efficiency
- can precompute audio embeddings, and match it up to different text queries
- can be built on current ALMs

### Logit Adjustment
- some classses occur more often than others, some events are longer than others
- most frame/text pairs are super negative.
- thus, there is a text-related logit bias applied to the pre-sigmoid dot product.
- dependencies are bad - what if you hear thunder, but then classifies it as rain, since rain is longer in the dataset.


## Experiments

### Sound event detection - graph
- dataset: a single example of audio mixture
- metrics: frame-wise prediction accuracy
- baselines: 

### Sound event detection performance
- dataset: synthetic open-vocabulary SED. 6 datasets
- metrics: AUROC, PSDS
- baselines: MGA-CLAP, and FLAM but global.

### retrieval
- text to audio, audio to text.
- 3 datasets
- baselines: FLAM global and MGA-CLAP (retrained on same dataset). also compared to LAION CLAP, CompA, MGA-CLAP, which were trained on different datasets.

## zero-shot classification
- baselines: MGA-CLAP, LAION,

### Ablations
- removing per-text scale, per-text bias, and both


Last Reviewed: 7/16/2025