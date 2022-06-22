# X-ab: Detecting abnormality in chest X-ray images

Automatic diagnosis of lung diseases from chest x-ray images is hard. The state-of-the-art model from the 2021 Kaggle competition [Nguyen et al, 2021] shows less than 40% accuracy in diagnosing 15 different lung diseases. However, health checkup centers may not need to diagnose different types of lung disease. Instead, they only need to prescreen *abnormal* chest x-ray images, and those prescreened as *abnormal* can be sent to a hospital for further inspection. This project is to build a deep learning model that prescreens *abnormal* chest x-ray images without doctors present.

There are a few technical challenges in developing the prescreening model, which are, (1) how to detect abnormal images without object detection, as normal images are just those *not* having abnormal spots and localizing abnormal spots is much difficult; (2) how to deal with the class imbalance problem, as there are much more normal images than abnormal images in practice so the model could be easily biased toward *normal* if trained without caution; and (3) how to estimate the confidence of each prediction (or the probability of being abnormal), as a prediction without confidnce is difficult to trust in patients.

To address these challenges, I developed a deep learning model, combining *EfficientNet* [Tan et al, 2019] and *cost-sensitive learning* [Lin et al, 2017]. The model showed over 94% f1-score on VinBigData. I am currently working on *model calibration* [Guo et al, 2017] to estimate the prediction confidence. Accurately diagnosing lung diseases without doctors’ presence are often dangerous, because the diagnosis itself is difficult and taking responsibility for a misdiagnosis is complicated. This prescreening model can relieve these two problems and save money by reducing espensive doctors' labor costs.

[Nguyen et al, 2021] VinDr-CXR: An open dataset of chest X-rays with radiologist’s annotations. arXiv2021. https://arxiv.org/pdf/2012.15029.pdf 

[Tan et al, 2019] EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks. ICML2019. https://arxiv.org/pdf/1905.11946.pdf

[Lin et al, 2017] Focal Loss for Dense Object Detection. CVPR2017. https://arxiv.org/abs/1708.02002

[Guo et al, 2017] On Calibration of Modern Neural Networks. ICML2017. https://arxiv.org/abs/1706.04599

