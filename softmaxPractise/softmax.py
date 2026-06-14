import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

num_epoch = 1000

#data listed as [no. legs], [eggs?], [hair?], [feathers?], [scales?], [label]
data = np.genfromtxt("softmaxPractise/animals.txt")
print(data)


