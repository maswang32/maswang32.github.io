# wav2vec

learn from speech audio alone


masks speech in latent space, solves a contrastive task, defined over a quantization of latent representations, which are jointly learned

uses a contrastive task

1-hour of labeled data, still beats 100 hours 

can work with just 10 minutes of labeled data, if 53k hours of pretraining data



CNN, then mask spans of the CNN output, then transformer




Finetuned with CTC loss later


also see vq-wav2vec


CNN: Audio -> Z

transformer: Z -> C

quantizer: Z -> Q

raw audio (not spectrogram), layer norm, GELU


instead of positional embeddings, use convolutional layer (i guess this is like, a convolution between adjacent tokens) - GeLU this, then apply layernorm

use product quantization on the zs, then linear projection

differentiate through the quantization layer using gumbel

## training
mask in Zs, training objective predicts the correct latent quantized category for masked tokens


Last Reviewed: 10/31/25 