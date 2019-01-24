import numpy as np


def cost_type(x: np.ndarray):
    x = np.array(x)
    Min = x.min()
    Max = x.max()
    x = (x - Min) / (Max - Min)
    return x


def benefit_type(x: np.ndarray):
    x = np.array(x)
    Min = x.min()
    Max = x.max()
    x = (Max - x) / (Max - Min)
    return x


def moderate_type(x: np.ndarray, s):
    x = np.array(x)
    Max = x.max()
    Min = x.min()
    if not (s > Min and s < Max):
        print("normalization error: the best value s is wrong")
    x = 1 - abs(x - s)/max(Max - s, s - Min)
    return x


if __name__ == "__main__":
    x = [1, 4, 7, 2]
    x = np.array(x)
    print(benefit_type(x))
    print(cost_type(x))
    print(moderate_type(x, 4))