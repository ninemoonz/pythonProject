import numpy as np

mat1 = np.arange(10).reshape(2, 5)
mat2 = np.arange(10).reshape(2, 5)
print(mat1)
print(mat2)

# approaching in order
print("mat1: ")
for i in range(mat1.shape[0]):
    for j in range(mat1.shape[1]):
        mat1[i, j] = mat1[i, j] * 2
print(mat1)

print("mat2: ")
for i in range(mat2.shape[0]):
    for j in range(mat2.shape[1]):
        mat2.itemset((i, j), mat2.item(i, j) * 2)
print(mat2)

