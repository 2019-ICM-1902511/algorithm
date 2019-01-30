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
