import read_data
import numpy as np

rc = np.zeros((4, 1))
rc_count = 0
industrial = np.zeros((4, 1))
industrial_count = 0
reservation = np.zeros((4, 1))
reservation_count = 0
algoriculture = np.zeros((4, 1))
algoriculture_count = 0

tmp = read_data.read_tmp()
l, _ = tmp.shape
for i in range(l):
    if type == 0:
        # rc
        rc += tmp[i][2: 6]
        rc_count += 1
    elif type == 2:
        industrial += tmp[i][2: 6]
        industrial_count += 1
    elif type == 3:
        reservation += tmp[i][2: 6]
        reservation_count += 1
    elif type == 4:
        algoriculture += tmp[i][2: 6]
        algoriculture_count += 1
w_rc = rc / rc_count
w_in = industrial / industrial_count
w_re = reservation / reservation_count
w_al = algoriculture / algoriculture_count
print(w_rc, w_in, w_re, w_al)
