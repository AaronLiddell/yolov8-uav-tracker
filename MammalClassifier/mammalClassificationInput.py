import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim


model = nn.Sequential(
    nn.Linear(3, 4),
    nn.ReLU(),
    nn.Linear(4, 1),
    nn.Sigmoid()
)

model.load_state_dict(torch.load("mammal_model.pth")) 
model.eval()  #into evaluation mode, disables dropout (which i didnt use)

unknown_input = [8, 1, 1]
unknown_tensor = torch.tensor(unknown_input, dtype=torch.float32)
unknown_output = model(unknown_tensor)
print(unknown_output)

animal_class_num = unknown_output[0].item()
if animal_class_num > 0.5:
    print(f"Animal is a mammal")
else:
    print(f"Animal is NOT a mammal")