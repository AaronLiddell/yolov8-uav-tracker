import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch.optim as optim

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
model_softmax.state_dict()

train_loader = DataLoader(train_data, batch_size=16)
val_loader = DataLoader(val_data, batch_size=16)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model_softmax.parameters(), lr=0.01)

epochs = 200
loss = []
acc = []


for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        optimizer.zero_grad()

        #flattens each image from 2D grid to 1D vector with 28*28=784 values
        #passes flattened image through model
        #stores the 10 resulting classes as outputs
        outputs = model_softmax(images.view(-1, 28*28))

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    loss.append(loss.item())
    correct = 0

    for images, labels in val_loader:
        outputs = model_softmax(images.view(-1, 28*28))
        
