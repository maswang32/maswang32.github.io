# Fast R-CNN

1. region proposal network creates a feature map
2. ROI pooling greates a fixed-size feature vector, which pools each patch into a fixed-size feature vector

Fast-R-CNN - region proposal network

features from the same CNN are pooled for classifications




## Paper
- problem with R-CNN is that it fine tunes a ConvNet, then fits an SVM to convnet features
- CNN proudces a feature map
- for each object proposal region of interest, we extract a fixed-length feature vector fro the feature map.
- each feature vectors  is passed through FC - one estimates K object class pus background, another that outputs 4 real-valued numbers for each of the K object classes
- 4 values refine bounding box positions
-ROI pooling uses max pooling



Last Reviewed: 10/28/2025