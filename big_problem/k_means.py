from sklearn.cluster import KMeans
import numpy as np
import read_data
import pix_bng
import scipy.misc

tmp = read_data.read_tmp()
l, wi = tmp.shape
X = tmp[:, 0:7]
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
labels = kmeans.labels_
labels = labels.reshape((l, 1))


result = np.hstack((tmp, labels))
np.savetxt('result.csv', result, delimiter=',')

centers = kmeans.cluster_centers_


labels = labels * 255 / max(labels)
img = read_data.read_map()
img_result = np.ones(img.shape)
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = labels[i]

scipy.misc.imsave('k_means.jpg', img_result)
