import torch
import torch.nn as nn #neural network

data = [1, 2, 3, 4, 5]
extra_data = [1, 3, 2, 3, 6]

tensor = torch.tensor(data)
error = torch.tensor(extra_data)

print(tensor)
print(tensor.shape)
print(tensor.dtype)

tensor_diff = tensor + error #addition
print(tensor_diff)
tensor_element_mult = tensor * error #element multiplied
print(tensor_element_mult)
tensor_matrix_mult = tensor @ error #matrix multiplied 
print(tensor_matrix_mult)

linear_layer = nn.Linear(5, 2, 2)
result = linear_layer(tensor)
print(f"Result: {result}")


