import torch
import numpy as np

a = torch.tensor([1.0, 2.0, 3.0])
M = torch.tensor([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])

print(a.shape, M.shape, M.dtype)
print(M[:, 1])
print(a * 2)
print(M + a)
print(M.sum(dim=0), M.sum(dim=1))
print(torch.arange(6).reshape(2, 3))
print(a @ a)

A = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
B = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
print(A @ B)

x = torch.randn(2, 3)
print(x.shape, x.T.shape)

n = np.array([1, 2, 3])
t = torch.from_numpy(n)
print(t, t.numpy())

print("GPU available:", torch.cuda.is_available())