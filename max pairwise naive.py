import numpy as np

n = input("Enter no of integers: ")
nos = np.array(list(map(int, input("Enter numbers: ").split())))
out = np.matmul(nos.reshape(-1, 1), nos.reshape(1, -1))
np.fill_diagonal(out, 0)
print(np.max(out))