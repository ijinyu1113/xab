# X-ab: Detecting abnormality in chest X-ray images

Thanks to deep learning-based AI technology and labeled chest X-ray images amassed in hospitals, chest X-ray abnormalities detection has gained attention based on deep learning technology. However, existing deep learning models have faced difficulties in correctly diagnosing lung diseases, due to (1) the diversities of the diseases and (2) the difficulties in correctly localizing the abnormal spots in X-ray images. For example, for VinBigData [Nguyen et al, 2021], the best accuracy achieved is 36.5% for classifying 15 diseases from chest X-ray images. We aim to develop deep learning models that detect and prescreen normal chest X-ray images, which is supposed to be easier than classifying the diverse diseases. This model can be used for AI health checkup, and those not prescreened by the model can be examined further by doctors.

There are a few technical challenges in developing the prescreening model, which are, (1) how to deal with the class imbalance problem, as there are much more normal images than abnormal images in practice; (2) how to detect normal images without object detection, as object detection is much difficult and normal images are those not having abnormal spots; and (3) how to estimate the confidence of each prediction. To address these challenges, I developed a deep learning model, combining EfficientNet [Tan et al, 2019] and a cost-sensitive learning [Lin et al, 2017]. The model showed over 94% f1-score on VinBigData. I am currently working on model calibration [Guo et al, 2017] to estimate the confidences of the predictions.

[Nguyen et al, 2021] VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations. arXiv2021. https://arxiv.org/pdf/2012.15029.pdf 

[Tan et al, 2019] EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML2019. https://arxiv.org/pdf/1905.11946.pdf

[Lin et al, 2017] Focal Loss for Dense Object Detection. CVPR2017. https://arxiv.org/abs/1708.02002

[Guo et al, 2017] On Calibration of Modern Neural Networks. ICML2017. https://arxiv.org/abs/1706.04599

