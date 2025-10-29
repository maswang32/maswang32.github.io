# SDEdit

Task - guided image synthesis - create/edit images w/ min. effort

previous = CGAN / GAN inversions, requires user annotations/training data or custom loss functions

SDEdit adds noise to the brush strokes, then denoises.

Can do stroke-based editing, or painting-to-image.


CGAN turns image into edited by training
GAN inversion turns the image into latent, then edits.

more noise = more realistic, less faithful.


stroke based synthesis: better in terms of realism and satisfication from users

compositing: better faithfulness, better user satisfaction



## Experiments

Tasks
- stroke-based image generation
    - metrics: user study for realism and faithfulness, L2, KID
    - 4 GAN-based baselines
- Stroke-based image editing
    - qualitative
- image blending
    -  metrics: L2, LPIPS within region that should be kept the same, user study for realism and faithfulness


### Figures
- Teaser figure (fig 1) showing image editing and stroke-based synthesis
- Fig 3: Plots showing tradeoff between KID and L2 squared (fig 3)
- fig 4 - qualitative comparisons to baselines
- fig 5 - conditional generation examples
- fig 6 - stroke-based editing examples

### Tables
- Comparing faithfulness, quality, and satisfication on stroke-based generation - two MTurk surveys asking about realism and satisfactory, and L2 faithfulness score - LSUN, CelebHQ. Use open-source models.
- L2, KID of LSUN bedroom/church. Simulated strokes.


### Baselines:
- in domain GAN 1
- in domain GAN 2
- styleGAN
- e4e


### Metrics
Realism - measured by humans or NN
faithfulness - similar to guide, L2 distance
User metrics on realism and faithfulness


### More Notes

Stroke based image editing:
- human-created guides
- simulated stroke paintings

-theoretical upper bound on guide and generation, based on L2 distance - to have a shot of being realistic need high noise level, to be faithful, noise level should not be too high. bad guides (white image) mean higher noise level needed - since the closest images to the input are quite far.
    - binary search for t0 based on user preference.
    - same t0 usually works for all reasonable guides in the same task.
- we can also mask out part of the image we do not want to edit - additional channel





## Related Work
Conditional GANs - trained on original and edited images, data collection, model retraining -

GAN inversion - input is projected into latent space of a GAN, code is modified, image is resynthesized - all need different losses for different tasks.

other generative models - less used for editing, choi 2021 does conditional image synthesis assuming conditions can be measured from the underlying true image.


### Other notes
unlike other inverse problems, do not know measurement function (image to sketch function)
realism and faithfulness are not positively correlated, there are random realistic images or 
use of score-based models to solve inverse problems and methods requiring paired datasets do not apply
key hyperparameter is t_0

experimental details in appendix
