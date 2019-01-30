# The folling code crawls the satellite image data to get the land use information.

# shenzhen satellite map
from PIL import Image
import numpy as np
from normalization import benefit_type


def loadImage():
    img = Image.open("D:\\code\\ICM\\algorithms\\data\\map.jpg").convert('RGB')
    return img


def is_red(x):
    d = abs(x - np.array([220, 98, 121]))
    print(d)
    return (d[0] <= 10 and d[1] <= 10 and d[2] <= 10)


def is_purple(x):
    d = x - np.array([161, 0, 204])

    return (d[0] <= 10 and d[1] <= 10 and d[2] <= 10)


def is_orange(x):
    d = x - np.array([248, 150, 61])
    return (d[0] <= 10 and d[1] <= 10 and d[2] <= 10)



def is_green_shallow(x):
    d = x - np.array([211, 239, 123])
    return (d[0] <= 10 and d[1] <= 10 and d[2] <= 10)



def is_green_deep(x):
    d = x - np.array([161, 196, 146])
    return (d[0] <= 10 and d[1] <= 10 and d[2] <= 10)



if __name__ != "__main__":
    img = loadImage()
    img = np.array(img)
    print(img.shape)
    '''
    max = img.max()
    min = img.min()
    print(max)
    print(min)
    print(img[700][800])
    '''

    count_red = 0
    count_green_shallow = 0
    count_green_deep = 0
    count_orange = 0
    count_purple = 0

    for i in range(1409):
        for j in range(1929):
            if is_red(img[i][j]):
                count_red += 1
            elif is_green_shallow(img[i][j]):
                count_green_shallow += 1
            elif is_green_deep(img[i][j]):
                count_green_deep += 1
            elif is_orange(img[i][j]):
                count_orange += 1
            elif is_purple(img[i][j]):
                count_purple += 1
    print((count_red, count_green_shallow, count_green_deep, count_orange, count_purple))

if __name__ == "__main__":
    count_red, count_green_shallow, count_green_deep, count_orange, count_purple = (258040, 80124, 59449, 32130, 42885)
    algriculture = count_green_shallow
    rc = count_red
    reservation = count_green_deep
    transport = count_orange + count_purple
    industrial = 0

    result = [rc, transport, industrial, reservation, algriculture]
    print(result)
    result = result / np.sum(result)
    print(result)


# British satellite map
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