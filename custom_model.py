# https://github.com/lukemelas/EfficientNet-PyTorch
import torch.nn as nn
from efficientnet_pytorch import EfficientNet


class MyEfficientNet(nn.Module):
    def __init__(self, model_name, out_features):
        super().__init__()

        # load pretrained EfficientNet
        self.network = EfficientNet.from_pretrained(model_name)

        # replace last layer
        print('out features: ', self.network._fc.in_features)
        self.network._fc = nn.Sequential(nn.Linear(self.network._fc.in_features, out_features))

    def forward(self, x):
        out = self.network(x)
        return out
