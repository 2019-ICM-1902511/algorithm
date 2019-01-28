import csv
import numpy as np
from PIL import Image


def read_data():
    path = "D:\\code\\ICM\\algorithms\\big_problem\\data\\jiahua.csv"  # TODO
    l0 = []
    li = []
    with open(path) as f:
        reader = csv.reader(f)
        for line in reader:
            for i in line:
                li.append(float(i))
            l0.append(li)
            li = []
    l0 = np.array(l0)
    return l0


def read_map():
    path = "D:\\code\\ICM\\algorithms\\big_problem\\data\\data.png"
    img = Image.open(path).convert("RGB")
    img = np.array(img)
    return img


def read_tmp():
    path = "D:\\code\\ICM\\algorithms\\big_problem\\data\\tmp.csv"
    l0 = np.loadtxt(open(path, "rb"), delimiter=",", skiprows=0)
    l0 = np.array(l0)
    return l0


if __name__ == "__main__":
    tmp = read_tmp()
    print(tmp)