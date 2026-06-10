import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

num_epoch = 10

# Each row = one animal: [limbs, eggs, hair]
data = [
    [4, 0, 1],
    [8, 1, 1],
    [2, 0, 1],
    [2, 1, 0],
    [6, 1, 0]
]

#1 is mammal, 0 is not mammal
label = [1, 0, 1, 0, 0]


input_tensor = torch.tensor(data, dtype=torch.float32)
size = input_tensor.shape
print(f"size: {size}")

model = nn.Sequential(
    nn.Linear(3, 4),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

criterion = nn.CrossEntropyLoss()

#creating optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(num_epoch):
    optimizer.zero_grad()

    output = model(input_tensor) #this is a forward pass

    loss = criterion(output, label)
    loss.backward()
    optimizer.step()



output = model(input_tensor)
print(output)