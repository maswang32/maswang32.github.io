# Rate Distortion Theory


autoencoder

distortion function = d(x, xhat)
R = average bits required to represent realization (e.g. number of channels)

R(D) - minimum rate needed (R) such that the expected distortion doesn't exceed D.

= infimum of the MI(X,Xhat) (input and reconstruction)
you want to minimize the MI between X and Xhat while maintaining the distortion constraint
(analogous to error being orthogonal to the line you fit)

R(D) must be equal to the entropy of the input to get perfect reconstruction


narrowest bottleneck constrains information through the network.

narrowest pipe constrains water flow.



Last Reviewed: 10/26/2025
