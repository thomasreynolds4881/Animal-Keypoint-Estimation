## Animal Pose Estimation Using RCNN With Keypoints
##### This is a final project for my Computer Vision class.

### Overview
The goal of this project was to predict the keypoints of various animals across different poses and domains. Each animal has an annotated bounding box and list of keypoints, and each image can include multiple animals. Keypoints can be missing if they are out of frame. I used a variation of RCNN to do this. RCNN is a well-known object detection algorithm within the computer vision domain. For this project, I used PyTorch's implementation of keypoint RCNN detection, which makes use of a framework called Mask R-CNN (https://arxiv.org/abs/1703.06870). This model is found within PyTorch as KEYPOINTRCNN_RESNET50_FPN.

### Files/Folders
- estimation.ipynb: notebook following RCNN detection experiment
- dependencies: files taken from pytorch, used for running model etc

### Data
I heavily modified the data credited below so that it would align with the specific Dataset class found in the tutorial I followed. I uploaded the dataset, split into Test and Train and then Images and Annotations, with a separate annotations.json file that was included with the original data. There are around 3000 training images and 600 testing images.
Link to data: https://drive.google.com/file/d/1WbVepGP3T5xTWRQiI35a4A4kS_7uauBS/view?usp=sharing

### Credit
Keypoint RCNN tutorial: https://medium.com/@alexppppp/how-to-train-a-custom-keypoint-detection-model-with-pytorch-d9af90e111da
Pytorch detection dependencies: https://github.com/pytorch/vision/tree/main/references/detection
Initial dataset: https://sites.google.com/view/animal-pose/
