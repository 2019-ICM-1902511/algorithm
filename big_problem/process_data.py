import numpy as np
import read_data
import get_land_type


def process_data():
    data = read_data.read_data()
    recreation = np.sum(data[:, 3:9], axis=1)
    recreation = np.array(recreation)
    l,  = recreation.shape
    recreation = recreation.reshape((l, 1))

    regulation = np.sum(data[:, 9:15], axis=1)
    regulation = np.array(regulation)
    regulation = regulation.reshape((l, 1))

    production_of_goods = np.sum(data[:, 15:21], axis=1)
    production_of_goods = np.array(production_of_goods)
    production_of_goods = production_of_goods.reshape((l, 1))

    urban_green = np.sum(data[:, 21:27], axis=1)
    urban_green = np.array(urban_green)
    urban_green = urban_green.reshape((l, 1))

    esv = np.sum(data[:, 30:36], axis=1)
    esv = np.array(esv)
    esv = esv.reshape((l, 1))

    E = data[:, 1]
    E = np.array(E)
    E = E.reshape((l, 1))

    N = data[:, 2]
    N = np.array(N)
    N = N.reshape((l, 1))

    types = get_land_type.get_land_type(E, N)
    types = np.array(types)
    types = types.reshape((l, 1))

    result = np.hstack((E, N, urban_green, regulation, recreation, production_of_goods, esv, types))
    print(result)
    np.savetxt('tmp.csv', result, delimiter=',')


if __name__ == "__main__":
    process_data()