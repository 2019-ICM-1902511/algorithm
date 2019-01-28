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


if __name__ == "__main__":
    print(en2lola(np.array([461000]), np.array([1217000])))
    print(en2xy(np.array([461000]), np.array([1217000])))

