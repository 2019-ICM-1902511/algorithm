import read_data
import numpy as np
import pix_bng
import scipy.misc


red = [220, 98, 121]
orange = [248, 150, 61]
green = [161, 196, 146]
colors = [green, orange, red]

# input
result = read_data.read_result()
l, _ = result.shape
labels = result[:, -1]
centers = read_data.read_centers()

class_color = np.zeros([30, 3])
cx, cy = pix_bng.en2xy(centers[:, 0], centers[:, 1])
print(cx, cy)
for i in range(30):
    if cy[i] > 850 and cx[i] > 400:
        class_color[i] = red
    elif cx[i] < 400:
        class_color[i] = green
    else:
        class_color[i] = orange


img = read_data.read_map()
img_result = np.ones(img.shape) * 255
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = class_color[int(labels[i])]
    for xs_n in range(xs[i] - 5, xs[i] + 5):
        for ys_n in range(ys[i] - 5, ys[i] + 5):
            try:
                img_result[xs_n][ys_n] = class_color[int(labels[i])]
            except IndexError:
                continue

scipy.misc.imsave('k2_means.jpg', img_result)

