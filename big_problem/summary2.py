# the following code is the the code when we apply our model to the cases,
# use k-means, w-means to compare to compare it with other models, and evaluate it

# the first time applying k-means (towards the locations of British)
from sklearn.cluster import KMeans
import numpy as np
import read_data
import pix_bng
import scipy.misc

# 得到数据
tmp = read_data.read_tmp()
l, wi = tmp.shape

# k-means 训练
# X = np.hstack((tmp[:, 0:2], tmp[:, 2:7]))
X = tmp[:, 0:2]
kmeans = KMeans(n_clusters=30, random_state=0).fit(X)
labels = kmeans.labels_
labels = labels.reshape((l, 1))
centers = kmeans.cluster_centers_

result = np.hstack((tmp, labels))
np.savetxt("D:\\code\\ICM\\algorithms\\big_problem\\data\\result.csv", result, delimiter=',')

np.savetxt('D:\\code\\ICM\\algorithms\\big_problem\\data\\centers.csv', centers, delimiter=',')

colors = labels * 255 / max(labels)
# colors = 255 - colors

img = read_data.read_map()
img_result = np.ones(img.shape) * 255
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = [labels[i]] * 3
    for xs_n in range(xs[i] - 5, xs[i] + 5):
        for ys_n in range(ys[i] - 5, ys[i] + 5):
            try:
                img_result[xs_n][ys_n] = [labels[i]] * 3
            except IndexError:
                continue

scipy.misc.imsave('k_means.jpg', img_result)

# the second k-means (towards to the projects(results of the first k-means) and their impacts on ecs)
import read_data
import numpy as np
import model
from sklearn.cluster import KMeans
import pix_bng
import scipy.misc


# input
result = read_data.read_result()
l, _ = result.shape
labels = result[:, -1]
print(max(labels), min(labels))
input_data = np.zeros((30, 5))

for i in range(30):
    for line in result:
        if line[-1] != i:
            continue
        land_type = line[-2]
        input_data[i][int(land_type)] += 1


input_data = input_data.astype("int")
evcs = [model.cal(x) for x in input_data]
evcs = np.array(evcs)
evcs = (evcs - 5)
print(evcs)
# k-means 训练
X = evcs
zeros = np.zeros(X.shape)
X = [(x, y) for x, y in zip(X, zeros)]
print(X)
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
labels = kmeans.labels_
print(labels)

red = [220, 98, 121]
orange = [248, 150, 61]
green = [161, 196, 146]
colors = [green, orange, red]

img = read_data.read_map()
img_result = np.ones(img.shape) * 255
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = colors[labels[int(result[i][-2])]]
    for xs_n in range(xs[i] - 5, xs[i] + 5):
        for ys_n in range(ys[i] - 5, ys[i] + 5):
            try:
                img_result[xs_n][ys_n] = colors[labels[int(result[i][-2])]]
            except IndexError:
                continue

scipy.misc.imsave('k2_means.jpg', img_result)


# convert between bng and pixel location
from convertbng.util import convert_bng, convert_lonlat
import numpy as np

'''
# convert a single value
def lalo2bng(lon: float, lat: float):
    return convert_bng(lon, lat)
'''


# convert lists of longitude and latitude values to OSGB36 Eastings and Northings, using OSTN15 corrections
def lola2en(lon: list, lat: list):
    lon = np.array(lon)
    lat = np.array(lat)
    return convert_bng(lon, lat)


# convert lists of BNG Eastings and Northings to longitude, latitude
def en2lola(eastings: list, northings: list):
    eastings = np.array(eastings)
    northings = np.array(northings)
    res_list_en = convert_lonlat(eastings, northings)
    return res_list_en


'''
# assumes numpy imported as np
lons_np = np.array(lons)
lats_np = np.array(lats)
    res_list_np = convert_bng(lons_np, lats_np)
'''


def xy2lalo(x, y):
    x = np.array(x)
    y = np.array(y)
    a1, b1, a2, b2 = (-0.00734380808080811, 61.1019318787879, 0.011208989247311823, -11.072256397849461)
    latitude = x * a1 + b1
    longtitude = y * a2 + b2
    return (latitude, longtitude)


def lola2xy(lo, la):
    lo = np.array(lo)
    la = np.array(la)
    a1, b1, a2, b2 = (-0.00734380808080811, 61.1019318787879, 0.011208989247311823, -11.072256397849461)
    x = (la - b1) / a1
    y = (lo - b2) / a2
    x = [int(i) for i in x]
    y = [int(i) for i in y]
    x = np.array(x)
    y = np.array(y)
    x = np.clip(x, 0, 1610)
    y = np.clip(y, 0, 1098)
    return (x, y)


def en2xy(E, N):
    E = np.array(E)
    N = np.array(N)
    return lola2xy(en2lola(E, N)[0], en2lola(E, N)[1])


