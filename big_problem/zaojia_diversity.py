import read_data
import numpy as np
import pix_bng
import scipy.misc


# input
result = read_data.read_result()
l, _ = result.shape

color = [161, 196, 146]
color = np.array(color)

target = result[:, 4] + result[:, 5] * 3
print(target)
target = (target - min(target)) / (max(target) - min(target))
target = [x * color for x in target]
target = np.array(target)
print(target)
target = target * 6
target = np.clip(target, 0, 255)
target = np.array(target)


img = read_data.read_map()
img_result = np.ones(img.shape) * 255
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = target[i]
    for xs_n in range(xs[i] - 3, xs[i] + 3):
        for ys_n in range(ys[i] - 3, ys[i] + 3):
            try:
                img_result[xs_n][ys_n] = target[i]
            except IndexError:
                continue

scipy.misc.imsave('D:\\code\\ICM\\algorithms\\big_problem\\data\\diversity.jpg', img_result)