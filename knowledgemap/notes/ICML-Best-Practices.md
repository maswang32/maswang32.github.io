# ICML Best Practices

- claims and problems: clearly state the problems addressed and claims made.
- soundness: clearly explain how the results substantiate the claims.
- honesty: identify technical assumptions/limitations
- significance: if it's a new problem, why is the problem important?
- self-containment: expert reader has a good chance of understanding the paper
- context: paper discusses prior work, how it is related to the contributions made, making it easier for future readers to understand why the problems being addressed are being targeted
- background: for readers not familiar, provides some background


## Writing
- title expresses main contribution
- abstract gives short, objective summary of contributions
- paper separates problem description from contributions
- paper has conceptual outline/psuedocode description of algorithms/methods
- random access: you can read the problem description, skim notation, then look at claims and justification
- proofread


## Theoretical Contributions
- assumptions are stated in a formal, clear way
- novel claims are formally stated
- self-contained: theorem statements should not require all previous context to understand
- non-trivial statements are proved
- intuitive arguments for why statements hold
- why is the new algorithm better than previous state of the art? what changed?
- the parts of proofs that are not new are generously attributed
- definitions for words that are non-standard
- all external results cited, with page number/theorem number if needed


## Computational Experiments
- explain why we do each experiment - what questions are answered?
- separate
    - design of experiment
    - description of experiment
    - results
    - interpretation of results
- experiments with randomness can be replicated, by setting seeds
- which algorithms are used to compute each metric, along with references for the metric, and number of runs
- instead of average/median, include distributional info (e.g. std if data is close to normally distributed)
- list all hyperparameters
- number/range of hyperparameter values
- source code required is in supp or appendix, made publicly available
- compute requirements, GPU/CPU models, OS, names/versions of relevant software/frameworks


## Datasets
- all novel benchmarks are included in appendix/supp
- will be made publicly available
- existing benchmarks are cited/publicly available
- ones that aren't public are described in detail (how benchmark was designed/how data was obtained/descriptive stats)


Last Reviewed 7/30/2025