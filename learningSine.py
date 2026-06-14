import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim

epochs = 1000

x = np.linspace(0, 4 * np.pi, 1000)
y = np.sin(x)

x_tensor = torch.tensor(x).reshape(-1, 1)
y_tensor = torch.tensor(y).reshape(-1, 1)

model = nn.Sequential(
    nn.Linear(1, 32),
    nn.ReLU(),
    nn.Linear(32, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

criterion = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr=0.01)

for i in range(epochs):
    optimizer.zero_grad()
    pred = model(x_tensor)
    loss = criterion(pred, y_tensor)
    loss.backward()
    optimizer.step()

    print(f"loss: {loss}")