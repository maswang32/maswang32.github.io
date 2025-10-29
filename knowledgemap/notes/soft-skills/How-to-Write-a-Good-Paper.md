# How to write a good paper
Talk by Bill Freeman, CVPR 2020, workshop on how to write a good review

## Good papers are the only ones that matter

only creative/original/good papers count, and bad papers actually hurt

graph of paper quality vs impact on career

outliers/unique papers/unusual papers are great.



## Research is a crowded marketplace
it's not a bunch of scholars poring over your manuscript - everyone is trying to get attention



## Structuring a paper (not the only way)

1. what is the problem we're addressing
 - why should the audience care? sometimes you must tell them

2. what are the other solutions, and why are they not satisfactory?
3. explain your ownn solution, compare with others, why is yours better
4. Related work, similar solutions applied to another problem

Wait to write a paper until you have something important to say

Example format:
1. Introduction
2. Related Work
3. Main Idea (e.g. image  model)
4. algorithm
    - e.g. estimating bur kernel
            - multiscale approach
            - user supervision
5. experiments
    - e.g., large blur, small blur, images with significant saturation
6. discussion
7. conclusion



## Introduction

you must make the paper easy to read - for people to tell what the paper is about, problem, why problem is interesting, what's new, what's not, what's neat


## Main Idea

can include a toy example
e.g. low, mid, high spatial bands look very different when you shift a wavelet

## Experiments 
experiments on examples people care about are required - need quantitative comparison against other algorithms
if it's a new problem, find a workaround - how might a reasonable person modify another algorithm, or use a disabled version of your algorithm as baseline

## Conclusions
Why is the world a better place, what can you do now

future work: bad to end off with "here's all the things we didn't do". There's no partial credit. It's also a list of ideas for people to steal.
say where the work will lead, in general directions.


## Writing Tips
Doing these tips takes another 2-3 days

### Keep the reader in mind
- what does the reader expect/know so far?
- reader is a guest in your house - anticipate their needs (oh, you're probably thirsty/oh you're probably wondering this)
- what are they curious about/what do they understand/what do they need to know next
- gie a talk before to your lab, gives it structure, see where people are confused/what didn't work


### omit needless works
- sentence has no needless works, paragraphs no needeless sentences
- can be long, but every word tells
- there's a list of phrases that can be shortened
- most authors are too wordy (too many words)
- concise writing is easier to glance at and get meaning from
- writing example
- benefits:
    - more espace for other things (figure, experiment, more detail onto something - papers are always a squeeze)
    - shorter = easier to understand
- work through the first draft and make it concise

### Readership
- Most only glance at title, some skim abstract/figures, some read every word
- readers who read every word are the most important, but the paper should also work for people who only look at figures/abstract
- should be possible to read in a hurry and get the main points
- want figures to be self-contained, including captions
    - captions should tell the reader what to notice about the figure

- Equations are mostly skimmed over, except the most basic (knuth) - paper should make sense when all but the simplest equations are replaced with grunts, and be smooth
    - identify equations with a phrase, so people won't have to memorize numbers

### Tone
- be kind and gracious to baselines, security, not competition - "we're all good", we're standing among greats, not that every other paper is bad
- don't oversell, hide drawbacks, and disparage
- "because the author was ___ I could trust the results" - best paper prize, 2020
- Be positive - more pleasurable to read than a paper that implies it is the only good paper around.
- convey the right impression of performance: be honest

## Titles
- Shiftable multiscale transforms should be "what's wrong with wavelets"


## The job of ACs is to reject 80% of papers.
- they're always looking for easy reasons to reject, since they need to reject that many papers, and it is basically their job to reject papers
- easy reasons:
    - promises undelivered
    - missing important references
    - too incremental
    - results not believable
    - poorly written
    - incorrect statementns
- 1/3 are obvious rejects, and 1-2 are ORALs that really stand out and are EASY to select
- borderline papers:
    - cockroach - not exciting, boring, well-written, incremental, ok reviews. 2/3 are accepted
    - puppy with 6 toes - easy to point flaws, but delightful, 2/3 rejected, but maybe Oral next time


## Other notes
- Good writing is rewriting
- for negative results - you have to be thorough in provivg "the answer is not here". A bad negative result paper could have negative results that just depend on the choices made in the paper, and are not comprehensive. still these papers are hard to get accepted
- talk to others, ask about if they think experiments are enough.
- Faculty candidates for MIT: instead of counting papers, count the good papers. don't start writing too late, require an outlier first (richard szeliski)
- author list - since only great papers matter, it's better to be one of many on a great paper than one of few on a mid paper. do whatever it takes to make the paper pbetter.
- ask them if they feel they should be an author, if they say yes, put them on.
- other references
    - how to get your SIGGRAPH paper rejected (1993)
    - ted adelson's informal guidelines
    - notes on technical writing (knuth)
    - what's wrong with these equations
    - fredo durand's notes on writing
    - ten simple rules for mathematical writing


Last Reviewed: 7/30/2025