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
