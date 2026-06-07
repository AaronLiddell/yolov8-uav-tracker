import torch
import torch.nn as nn
import numpy as np

limbs = [4, 8]
eggs = [0, 1]
hair = [1, 1]

data = [[limbs],[eggs],[hair]]
print(data)

input_tensor = torch.tensor(data)
print(input_tensor)