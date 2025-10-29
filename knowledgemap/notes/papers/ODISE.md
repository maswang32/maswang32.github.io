# ODISE
Open-vocabulary Diffusion-based panoptic segementation

k-means clustering of diffusion model's internal representation

Use both CLIP and SD


Previous methods just use CLIP, but this not good for scene-level understanding, bad spatial relations between objects.

diffusion models compute cross attention between text embedding and interal visual representation

Fig 1, simply clustering diffusion model's internal features does some segmentation

diffusion model -> mask generator of all possible concepts, trained with annotated masks, categorizes each mask into many categories by associating with text embeddings.


## Training
- sample a noisy image
- feed it into the unit, with the captions
- the diffusion model's visual representation for x depends on its caption
- use implicit captioner when the caption is not available.
    - instead of using a network to generate captions, get an implicit text embedding, using CLIP, MLP to implicit text embedding.
    - only finetune the MLP


### Mask generator
- mask generator outputs N class-agnositc binary masks, can be any panoptic segementation network
- pixel wise BCE loss, along with ground-truth masks
- mask GT category label: if we have a lot of categories in the training set, encode all catgoeis with the frozen text encoder, then use a classification loss betwen all the training categories.
- the probability is Softmax( net_out dot Text_encoder(C_train)) (this is probably what allows it to generalize).


### Image caption supervision
- extract nouns from each caption, treat them as grounding category labels
- compute the simliarty between each image caption pair, with a grounding loss encouraging each noun to beg rounded by one  or a few masked regions in the image.


## Grounding loss
- the loss is overall image-word similarity, you take the probability of mask embedding features z_i with each word, times (z_i, T(w_k)).
- so it's two similarities, both against all the words  in the caption.
- avoids penalizing regions that are not grounded by any word


still have to keep reading


Last Reviewed: 10/28/2025