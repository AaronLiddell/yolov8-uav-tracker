import torch
import torch.nn as nn #neural network

data = [1, 2, 3, 4, 5]
extra_data = [1, 3, 2, 3, 6]

tensor = torch.tensor(data, dtype=torch.float32)
error = torch.tensor(extra_data)

print(tensor)
print(tensor.shape)
print(tensor.dtype)

tensor_diff = tensor + error #addition
print(tensor_diff)
tensor_element_mult = tensor * error #element multiplied
print(tensor_element_mult)
#tensor_matrix_mult = tensor @ error #matrix multiplied (doesnt work with float data type)
#print(tensor_matrix_mult)

linear_layer = nn.Linear(5, 2, 1) 
#(number of inputs, number of outputs, True(1)/False(0) to include bias)
#currently weight matrix is random so output in meaningless
#input (5 numbers) x weight matrix (5x2) + bias (2 numbers) = output (2 numbers)

result = linear_layer(tensor)
print(f"Result: {result}")


