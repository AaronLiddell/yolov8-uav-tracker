import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(5, 16),
    nn.ReLU(),
    nn.Linear(16, 3),
)

model.load_state_dict(torch.load("softmaxPractise/animal_model.pth"))
#model.eval()

#data listed as [no. legs], [eggs?], [hair?], [feathers?], [scales?], [label]
unknown_input = [0,1,0,0,0]
unknown_tensor = torch.tensor(unknown_input, dtype=torch.float32)

unknown_output = model(unknown_tensor)
print(unknown_output)

mamNum = unknown_output[0].item()
birdNum = unknown_output[1].item()
repNum = unknown_output[2].item()

if mamNum > birdNum and mamNum > repNum:
    print(f"MAMMAL")
elif birdNum > mamNum and birdNum > repNum:
    print("BIRD")
else:
    print("REPTILE")