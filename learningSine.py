import torch
import torch.nn as nn
import numpy as np
import torch.optim as optim
import matplotlib.pyplot as plt

epochs = 5000

x = np.linspace(0, 2 * np.pi, 4000)
y = np.sin(x)

x_tensor = torch.tensor(x).float().reshape(-1, 1)
y_tensor = torch.tensor(y).float().reshape(-1, 1)

model = nn.Sequential(
    nn.Linear(1, 32),
    nn.LeakyReLU(negative_slope=0.05),
    nn.Linear(32, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

criterion = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.97)

loss_array = []
epoch_array = []
for i in range(epochs):
    optimizer.zero_grad()
    pred = model(x_tensor)
    loss = criterion(pred, y_tensor)
    loss.backward()
    optimizer.step()

    print(f"loss: {loss}")

    loss_array.append(loss.item())
    epoch_array.append(i)

np_pred = pred.detach().numpy()

plt.plot(x, np_pred, label="Learned sine")
plt.plot(x, y, label="True sine")
plt.legend()
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Learning sine")
plt.show()

plt.plot(epoch_array, loss_array)
plt.xlabel("Epoch number")
plt.ylabel("loss")
plt.title("loss against epoch")
plt.show()