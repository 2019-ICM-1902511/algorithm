from sklearn import metrics as mr
import math


def mutual_info(x, y):
    return mr.mutual_info_score(y, x)


if __name__ == "__main__":
    x = [1, 2]
    y = [1, 2]
    print(mutual_info(x, y))
    print(math.log1p(1))
