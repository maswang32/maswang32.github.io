# Mask-RCNN

additional branch from Fast R CNN that predicts segmentation masks from a region.
produces bounding boxes


faster-RCNN already has claass label and bounnding box offset

Mask-RCNN wants to also give you a mask, but requires fine spatial layouts


multi-task loss - classification, bounding box, and mask.


mask loss is sigmoid, binary cross entropy.



# key
not semantic segmentation, which does a softmax and multinomail cross entropy loss on each pixel - instead, per-pixel sigmoid, doucpling mask and class prediction.

use a FCN for predicing an m x m mask.


# ROI align
ROI pool extracts a small 7x7 feature map from each ROI

it quantizes a floating-number ROI to the granuarliy of feature map.

instead of quantization, using blinear interpolation on the feature map, no quanization/rounding




Last Reviewed: 10/28/2025