import read_data
import numpy as np
import pix_bng
import scipy.misc


# input
result = read_data.read_result()
l, _ = result.shape

green = [161, 196, 146]
green = np.array(green)

urban_green = result[:, 3] * 2 + result[:, 4] * 4
print(urban_green)
urban_green = (urban_green - min(urban_green)) / (max(urban_green) - min(urban_green))
urban_green = [x * green for x in urban_green]
urban_green = np.array(urban_green)
print(urban_green)
urban_green = urban_green * 20
urban_green = np.clip(urban_green, 0, 255)
urban_green = 255 - urban_green
urban_green = np.array(urban_green)


img = read_data.read_map()
img_result = np.ones(img.shape) * 255
xs, ys = pix_bng.en2xy(result[:, 0], result[:, 1])
for i in range(l):
    img_result[xs[i]][ys[i]] = urban_green[i]
    for xs_n in range(xs[i] - 3, xs[i] + 3):
        for ys_n in range(ys[i] - 3, ys[i] + 3):
            try:
                img_result[xs_n][ys_n] = urban_green[i]
            except IndexError:
                continue

scipy.misc.imsave('D:\\code\\ICM\\algorithms\\big_problem\\data\\urban_green.jpg', img_result)
