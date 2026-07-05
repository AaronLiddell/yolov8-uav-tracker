import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

num_epoch = 5000

#get and separate data
#data listed as [no. legs], [eggs?], [hair?], [feathers?], [scales?], [label]
data = np.genfromtxt("softmaxPractise/animals.txt")
animal_info = data[:, :5]
animal_type = data[:, 5]

#turn them into tensors
training_tensor = torch.tensor(animal_info, dtype=torch.float32)
labels = torch.tensor(animal_type, dtype=torch.long)

model = nn.Sequential(
    nn.Linear(5, 16),
    nn.ReLU(),
    nn.Linear(16, 3),
)

criterion = nn.CrossEntropyLoss() #loss function (internally includes the softmax function)

optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(num_epoch):
    optimizer.zero_grad()
    pred = model(training_tensor) #gets predictions from model 
    loss = criterion(pred, labels) #calcs the loss (how wrong predictions are)
    loss.backward() #backproagates to find which weights caused the error
    optimizer.step() #updates weights to slightly reduce error

    print(f"loss: {loss}")

#output = model(training_tensor)

torch.save(model.state_dict(), "animal_model.pth") #saves the learned weights (not the model architecture)
