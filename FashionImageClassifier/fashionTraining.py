import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

from torchvision import datasets

import matplotlib.pyplot as plt

train_data = datasets.FashionMNIST(root="FashionImageClassifier/data", train=True, download=False)
train_data = list(train_data)[:4000]

#plot first 10 images from training data
for i, (img, label) in enumerate(train_data[:10]):
    plt.subplot(4, 3, i+1)
    plt.imshow(img, cmap="grey")
    print(label)

plt.show()