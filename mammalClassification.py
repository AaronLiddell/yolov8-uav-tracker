import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

num_epoch = 5000

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
label = torch.tensor(label, dtype=torch.float32).unsqueeze(1) #label must be tensor shape (5,1)

input_tensor = torch.tensor(data, dtype=torch.float32)
size = input_tensor.shape
print(f"size: {size}")

model = nn.Sequential(
    nn.Linear(3, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

criterion = nn.BCELoss() #correct loss function for binary classification

#creating optimizer
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(num_epoch):
    optimizer.zero_grad()

    output = model(input_tensor) #this is a forward pass

    loss = criterion(output, label)
    print(f"loss: {loss}")
    loss.backward()
    optimizer.step()



output = model(input_tensor)
print(f"Output:{output}")

#for i in len(output):
 #   if output[i] >= 0.5:
  #      print(f"Animal {i} is a mammal")
   # else:
    #    print(f"Animal {i} is not a mammal")

unknown_input = [4, 1, 0]
unknown_tensor = torch.tensor(unknown_input, dtype=torch.float32)
unknown_output = model(unknown_tensor)
print(unknown_output)

animal_class_num = unknown_output[0].item()
if animal_class_num > 0.5:
    print(f"Animal is a mammal")
else:
    print(f"Animal is NOT a mammal")