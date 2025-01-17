# Efficient K-Means Image Segmentation

In this project, conventional k-means clustering algorithm is implemented for both gray-scale and colored image segmentation.

The K-means algorithm is an unsupervised clustering method which classifies input data points into multiple classes based on their inherent distance from each other. It assumes that the data features form a vector space and attempts to find natural clustering within them.

The script `kmeans.py` uses the ideal output segmentation file (out1.jpg) to calculate/evaluate the accuracy of the segmentation for the gray-scale image. The code outputs TP rate, FP rate, and F-score.

Similarly, `kmeans_color.py` uses the ideal output segmentation file (out2.jpg) to calculate/evaluate the accuracy of the segmentation for the colored image. The code outputs TP rate, FP rate, and F-score.

This repo has been maintained by fanconnie.