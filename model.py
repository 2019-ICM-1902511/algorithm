import numpy as np


input = [0.5459685, 0.15871891,  0,          0.12578391,  0.16952868]
input = np.array(input)
W = [[0.28,   0.35, 0,   0.25,  0.11],
    [0.27,  0.3,   0.09,  0.12,  0.22],
    [0.21,  0.2,   0.23,  0.14,  0.23],
    [0.24, 0.09, 0.21, 0.13, 0.34],
    [0, 0.39, 0, 0.32, 0.29]]
W = np.array(W)
b = input.dot(W)  # 第三层的减少量
print(b)
We = [0.20, 0.35, 0.08, 0.16, 0.21]
We = np.array(We)
t = [x/w for x, w in zip(b, We)]
print(t)
result = sum(t)
print(result)