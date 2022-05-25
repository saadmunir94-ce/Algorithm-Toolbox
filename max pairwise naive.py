import numpy as np

n = input("Enter no of integers: ")
nos = list(map(int, input("Enter numbers: ").split()))
print(nos)
print(np.array(nos))
