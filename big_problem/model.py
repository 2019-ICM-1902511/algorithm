import numpy as np


def cal(inputs):
    inputs = np.array(inputs)
    inputs = inputs / np.sum(inputs)
    W = [[0.28,   0.35, 0,   0.25,  0.11],
        [0.27,  0.3,   0.09,  0.12,  0.22],
        [0.21,  0.2,   0.23,  0.14,  0.23],
        [0.24, 0.09, 0.21, 0.13, 0.34],
        [0, 0.39, 0, 0.32, 0.29]]
    W = np.array(W)
    b = inputs.dot(W)  # 第三层的减少量
    We = [0.20, 0.35, 0.08, 0.16, 0.21]
    We = np.array(We)
    t = [x/w for x, w in zip(b, We)]
    result = sum(t)
    return result