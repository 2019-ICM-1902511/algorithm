import pix_bng
import numpy as np
import read_data


agriculture = [115, 38, 0]
urban = [0, 0, 0]
suburban = [129, 129, 129]
white = [225, 225, 225]
sea = [0, 0, 128]


def is_true(x, y):
    d = abs(x - y)
    for i in d:
        if i > 10:
            return False
    return True


def get_type(x, y):
    print(x, y)
    img = read_data.read_map()
    if is_true(img[x][y], urban):
        return 0  # rc 
    elif is_true(img[x][y], suburban):
        return 2  # indus
    elif is_true(img[x][y], agriculture):
        return 4  # agri
    else:
        return 3  # re


def get_land_type(E: np.ndarray, N: np.ndarray):
    x, y = pix_bng.en2xy(E, N)
    types = [get_type(i, j) for i, j in zip(x, y)]
    types = np.array(types)
    return types


if __name__ == "__main__":
    data = read_data.read_data()
    E = data[:, 1]
    N = data[:, 2]
    print(get_land_type(E, N))
