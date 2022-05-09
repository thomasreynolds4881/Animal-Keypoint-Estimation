## Animal Pose Estimation Using RCNN With Keypoints

### Overview

The goal of this project was to predict the keypoints of various animals across different poses and domains. Each animal has an annotated bounding box and list of keypoints, and each image can include multiple animals. Keypoints can be missing if they are out of frame. I used a variation of RCNN to do this. RCNN is a well-known object detection algorithm within the computer vision domain. For this project, I used PyTorch's implementation of keypoint RCNN detection, which makes use of a framework called Mask R-CNN (https://arxiv.org/abs/1703.06870). This model is found within PyTorch as KEYPOINTRCNN_RESNET50_FPN.

![image](https://user-images.githubusercontent.com/48138681/167097671-5b1df808-4d8a-4d6c-984f-cb58f31049a7.png)

### Files/Folders

- estimation.ipynb: notebook following RCNN detection experiment
- dependencies: files taken from pytorch, used for running model etc

### Dataset

I heavily modified the data credited below so that it would align with the specific Dataset class found in the tutorial I followed. I uploaded the dataset, split into Test and Train and then Images and Annotations, with a separate annotations.json file that was included with the original data. There are around 3000 training images and 600 testing images. The images include sheep, horses, dogs, and cats.

![image](https://user-images.githubusercontent.com/48138681/167097274-0a4f4e6f-190a-4bc6-8a89-b85d9d1f713a.png)
![image](https://user-images.githubusercontent.com/48138681/167097331-1e12ea81-0152-409b-a62b-f329dc2dd0ed.png)
![image](https://user-images.githubusercontent.com/48138681/167097429-3a9ac2e0-aa31-49eb-aaa5-da9dc723c9a3.png)
![image](https://user-images.githubusercontent.com/48138681/167097488-d9f072d3-ee1d-4ec5-8490-a7f812483df7.png)

Link to data: https://drive.google.com/file/d/1WbVepGP3T5xTWRQiI35a4A4kS_7uauBS/view?usp=sharing

### Credit

- Keypoint RCNN tutorial: https://medium.com/@alexppppp/how-to-train-a-custom-keypoint-detection-model-with-pytorch-d9af90e111da
- Pytorch detection dependencies: https://github.com/pytorch/vision/tree/main/references/detection
- Initial dataset: https://sites.google.com/view/animal-pose/
