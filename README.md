# xab
## Detecting abnormality in chest X-ray images

Thanks to deep learning-based AI technology and labeled chest X-ray images amassed in hospitals, chest X-ray abnormalities detection has gained attention based on deep learning technology. However, existing deep learning models have faced difficulties in correctly diagnosing lung diseases, due to (1) the diversities of the diseases and (2) the difficulties in correctly localizing the abnormal spots in X-ray images. For example, for VinBigData [Nguyen et al, 2021], the best accuracy achieved is 36.5% for classifying 15 diseases from chest X-ray images. We aim to develop deep learning models that detect and prescreen normal chest X-ray images, which is supposed to be easier than classifying the diverse diseases. This model can be used for AI health checkup, and those not prescreened by the model can be examined further by doctors.

There are a few technical challenges in developing the prescreening model, which are, (1) how to deal with the class imbalance problem, as normal images are much larger than abnormal images, (2) how to detect normal images without object detection, as object detection is much difficult and normal images are those not having abnormal spots, and (3) how to compute the confidence of each prediction. To address these challenges, I developed a deep learning model, combining EfficientNet [Tan et al, 2019], a cost-sensitive learning [Lin et al, 2017] and a model calibration techniques []. This model showed over 94% f1-score on VinBigData.

[Nguyen et al, 2021] VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations. arXiv2021. https://arxiv.org/pdf/2012.15029.pdf 
![image](https://user-images.githubusercontent.com/68576111/174403274-f69286f7-c352-466b-acd7-38c80a407141.png)

[Tan et al, 2019] EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML2019. https://arxiv.org/pdf/1905.11946.pdf ![image](https://user-images.githubusercontent.com/68576111/174403235-a4bfec16-3b2b-41b9-9323-992c57104dcc.png)

[Lin et al, 2017] Focal Loss for Dense Object Detection. CVPR2017. https://arxiv.org/abs/1708.02002 ![image](https://user-images.githubusercontent.com/68576111/174403377-912d7f45-a344-4f30-83cb-40ed76d18823.png)

[Guo et al, 2017] On Calibration of Modern Neural Networks. ICML2017. https://arxiv.org/abs/1706.04599

