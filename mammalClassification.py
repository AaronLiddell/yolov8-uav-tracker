import torch
import torch.nn as nn
import numpy as np

# Each row = one animal: [limbs, eggs, hair]
data = [
    [4, 0, 1],  # animal 1
    [8, 1, 1],  # animal 2
]


input_tensor = torch.tensor(data, dtype=torch.float32)
size = input_tensor.shape
print(f"size: {size}")

sequential_layers = nn.Sequential(
    nn.Linear(3, 4),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

output = sequential_layers(input_tensor)
print(output)