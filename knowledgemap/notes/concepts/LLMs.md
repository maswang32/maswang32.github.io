# LLMs
- Language
- knowledge
- retreival and tool use
- in-context learning (learn new skills quickly)
- alignment
- capability 
- safety
- reasoning

reinforcement learning, give rewards
- how does it know the reason it succeeded?
- does random stuff if you don't pretrain


Language = special, natural domain for studying AI, this is the modality of the frontier.

supervised learning
- question answer pairs
SQuAD - QA dataset 2016.
- HotPotQA - pairs of wikipedia pages '18.
- MS Marco - 1,000,000 Bing Queries.
- MS Marco
- Natural Questions

Scale.
- self supervised learning (LLMs in machine translations 2007, ngrams)
- 1-10T trillion params GPT-5.

People are very conservative due to cost of training


post-training
- teachin LLMs to be instruction following assistants, effective at math, coding, using tools.


Now there are many stages:

pretraining - base data mixture, more code data-mixture, even more code + synthetic data mixture
- training on code is hypothesized to improve reasoning in general.

midtraining - context expansion, reasoning heavy

post-training: SFT, DPO / RL



open research
open models
open source (not open weights) like llama 1-4
open development


tokenization - word-based - misspellings, will encounter things you haven't seen beofre.


characters - lots of sequences. representation for "c" not very meaningful.


subword tokens.


## Pre-training
Don't use BERT
1 - only learning about the masked word, inefficient
2 - if you want to make it useful, need to generate text. instead of classifying something, just give the word of the class.
3 - encode all tokens during scratch

web knowledge - factual, syntax + coreference, sentiment, math, prompting.

design structures into your weights

start with some links, hop to adjacent links - most of the web is gibberish
oversample wikipedia, arXiv, GitHub, Reddit, StackExchange. People ask questions on reddit, multiple answers, upvotes, links - pages linked to from reddit posts or wikipedia.

can ask an LLM

## Long Contexts
pretraining = 4000 word context window
midtraining - longer, million/half a million tokens

100 H100s = small LLMs

Babysit training runs, look for spikes, track evals.

## Tweaks to transformer
- lots of small tweaks - mixture of experts, marin 8B


## how to budget compute
- 50 models? pick best?
- tune hyperparams at small scale/ No
- answer: scaling laws.

Last Reviewed: 10/26/2025
