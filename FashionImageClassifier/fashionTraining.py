import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

from torchvision import datasets, transforms

import matplotlib.pyplot as plt

train_data = datasets.FashionMNIST(root="FashionImageClassifier/data", train=True, download=False, transform=transforms.ToTensor())
train_data = list(train_data)[:4000]


def firstImages():
    #plot first 10 images from training data
    for i, (img, label) in enumerate(train_data[:10]):
        plt.subplot(4, 3, i+1)
        plt.imshow(img, cmap="grey")
        print(label)

    plt.show()

#splitting into training and validation
train_data, val_data = train_data[:3500], train_data[3500:]


class Softmax(nn.Module): #nn.Module is the base class for all neural network models in PyTorch
    
    def __init__(self, n_inputs, n_outputs):
        super().__init__() #required to initialize the parent class
        self.linear = nn.Linear(n_inputs, n_outputs)

    def forward(self, x):
        pred = self.linear(x)
        return pred
    

model_softmax = Softmax(784, 10)
print(model_softmax.state_dict())