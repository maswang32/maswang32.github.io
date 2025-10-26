# MIDI-DDSP



Chaining several systems together improves controllability


Some people combine MIDI with traditional DSP, but this is hard to generate realistic timbre.

Vision has systems optimized for both realism and control

concatentative systems have realism, but manual stitching limits control and expression.



analysis:
audio -> ddsp parameters -> performance -> notes

synthesis:
notes -> performance -> ddsp parameters -> audio

composer usually writes notes, performer interprets, then instrument converts to sound.
Notes, performance, synthesis.


three modules:
ddsp synthesizer, synthesis param generator, and expression generator.

three fixed feature extractions:
ddsp synthesis, feature extraction, note detection


requires pitch detection/note detection, so limited to single monophonic instruments.

train on > 12 instruments with a single model, conditional generation on instruments for every stage.


### Contributions
- extraction of note expression attributes
- control through manipulating different parts of the hierarchy - expert musicians can adjust parameters.
- reconstruction 
- prediction of synthesis params from notewise expressions
- realsitic note synthesis that is better than neural and professional concatentative approaches, according to user studies
- automatic music generation, generate Coconet then generate params


## Method
- supervision happens at each stage (not end to end)


## Skipped
Related work


Last Reviewed 10/8/25