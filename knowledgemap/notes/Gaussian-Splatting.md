# Gaussian Splatting
Super Fast Rendering - realtime display rates at 1080p
Higher quality than Mip-Nerf
Avoids unnecessary computation in empty space

Nerf and voxel-based 3D representations require stochastic sampling for rendering - computationally expensive, result in noise

use sparse point clouds obtained from SFM - no need for MVS
1-5 million gaussians per scene

Rendering:
-respect visibility ordering
-sorting
-tile-based rasterization


opacity-based rendering --- 
---the 'opacity' (light absorption) assigned to a point
depends on the distance from the previously sampled point, AND the density at the point
basically, you are assuming the 'point' is a block that absorbs light

These are continuous representations, (not voxels)
works with randomly initalized gaussians
can project gaussians to 2D and perform alpha blending

Parametrize each gaussian with:
    opacity, anisotropic covariance, spherical harmonics
    
adaptive density control - add or remove gaussians during training
Last Reviewed: 1/17/25
