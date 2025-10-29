# R-CNN
R-CNN - regional propsoal network - split object detection into two stages - first propose region, then classify object


get a bunch of region proposals using "selective search" (merges simlar regions using algorithms)


regize each region to 227 x 227 size, after dilating the bounuding box

selective search has fast mode during test time


SVM on feature vectors trained for that class, do non-maximum suppression to remove overlapping regions, by rejecting a region with an IoU of a higher scoring region


## Trainingss
- strain the CNN on a dataset using image-level annotation (imagenet)
- domain adapt using warped region proposals, replace linear layer
- greater than 0.5 IoU with ground truth box as positivies, lower learning rate by 0.1, 32 positive windows, 96 background windows.
- biased sampling toward positive windows.
- 0.3 IoU overlap thresehold between positive and negative examples, determined by validation set.
- optimize one linear SVM per class
- hard negative mining



selective search generates 2000 candidate recatngles, and linear regression prediccts 4 offsets





first, generate region proposals likely to contain objects (bounding boxes)

each region is cropped and resized (ROI polling)

feature extraction - CNN extracts features

object classification and bounding box regression - determine object class, and refine coordinates.

produces bounding boxes, not segmentation masks

Last Reviewed: 10/28/2025