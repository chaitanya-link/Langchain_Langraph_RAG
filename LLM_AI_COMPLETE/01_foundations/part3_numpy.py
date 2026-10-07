import numpy as np

a = np.array([1, 2, 3])
M = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.shape)       # (3,)
print(M.shape)       # (2, 3)  -> 2 rows, 3 columns
print(M[0])          # first row
print(M[:, 1])       # second column

print(a * 2)         # every number doubled
print(M + a)         # broadcasting: a is added to each row
print(M.sum(axis=0)) # collapse rows -> sum of each column
print(M.sum(axis=1)) # collapse columns -> sum of each row

print(np.arange(6).reshape(2, 3))

print(np.dot(a, a))  # dot product: 1*1 + 2*2 + 3*3

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)         # matrix multiplication