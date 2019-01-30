# the following code is the code when we establish the evaluaion model

# calculate the weight of the ahp model
import numpy as np
import csv
import re


np.set_printoptions(precision=2)


class AHP:
    def __init__(self, array):
        self.row = len(array)  
        self.col = len(array[0]) 
        self.array = array

    def get_tezheng(self, array):  
        np.set_printoptions(precision=2)
        te_val, te_vector = np.linalg.eig(array)  
        list1 = list(te_val)  
        print(np.abs(te_val))
        print(np.abs(te_vector))


        max_val = np.max(list1)  
        index = list1.index(max_val)  
        max_vector = te_vector[:, index]  
        print(str(max_val)+str(max_vector))
        return max_val, max_vector

    def RImatrix(self, n):  
        np.set_printoptions(precision=2)
        d = {}
        n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n2 = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45]
        for i in range(n): 
            d[n1[n]] = n2[n]
        print("RI = ", np.abs(d[n1[n]]))
        return d[n1[n]]

    def test_consitstence(self, max_val, RI):  
        np.set_printoptions(precision=2)
        CI = (max_val-self.row)/(self.row-1) 
        CR = CI/RI  
        if CR < 0.10:
            print("CR=  " + str(CR) + "pass the test")
            return True
        else:
            print("CR=  " + str(CR) + "fail the test")
            return False

    def normalize_vector(self, max_vector): 
        np.set_printoptions(precision=2)
        vector_after_normalization = []  
        sum0 = np.sum(max_vector)  
        for i in range(len(max_vector)):
            vector_after_normalization.append((max_vector[i]/sum0))

        print(str(vector_after_normalization))
        return vector_after_normalization

    def weightCalculator(self, normalMatrix): 
        np.set_printoptions(precision=2)
        listlen = len(normalMatrix) - 1  
        layerWeights = list() 
        while listlen > -1:
            sum = float()  
            for i in normalMatrix:
                sum += i[listlen]  
            sumAverage = round(sum / len(normalMatrix), 3) 
            layerWeights.append(sumAverage) 
            listlen -= 1
        return layerWeights


class AHP_method:
    def __init__(self, path: str):
        np.set_printoptions(precision=2)
        l0 = []
        l1 = []
        li = []
        with open(path) as f:
            reader = csv.reader(f)
            for line in reader:
                print(line)
                if line == []:
                    l1.append(l0)
                    l0 = []
                    continue
                for i in line:
                    if "/" in i:
                        if re.search("\d\s\d/\d", i) is not None:
                            b = i.split("/")
                            c = b[0].split(" ")
                            li.append(int(c[0]) + int(c[1]) / int(b[1]))
                        else:
                            b = i.split("/")
                            li.append(int(b[0]) / float(b[1]))
                    else:
                        li.append(float(i))
                l0.append(li)
                li = []
            l1.append(l0)
        print(l1)
        self.arrays = l1

    def test_consitstence(self):
        np.set_printoptions(precision=2)
        weigh_matrix = []
        for i in self.arrays:
            a = AHP(i)
            max_val, max_vector = a.get_tezheng(i)
            record_max_vector = max_vector
            RI = a.RImatrix(len(i))
            flag = a.test_consitstence(max_val, RI)
            while not flag:
                print("fail the test, please change the input matrix")
                break
            weight = a.normalize_vector(record_max_vector) 
            weigh_matrix.append(weight)
        print("the final weight is ", weigh_matrix)
        return weigh_matrix


# reader the .nc satellite data file
from netCDF4 import Dataset

nc_obj = Dataset('D:\\code\\ICM\\algorithms\\data\\had.nc')


print(nc_obj)
print('---------------------------------------')


print(nc_obj.variables.keys())
for i in nc_obj.variables.keys():
    print(i)
print('---------------------------------------')


print(nc_obj.variables['latitude'])
print(nc_obj.variables['longitude'])
print(nc_obj.variables['time'])
print(nc_obj.variables['temperature_anomaly'])
print(nc_obj.variables['field_status'])
print('---------------------------------------')


print(nc_obj.variables['latitude'].ncattrs())
print(nc_obj.variables['longitude'].ncattrs())
print(nc_obj.variables['time'].ncattrs())
print(nc_obj.variables['temperature_anomaly'].ncattrs())
print(nc_obj.variables['field_status'].ncattrs())

print('---------------------------------------')


print(nc_obj.variables['latitude'][:])
print(nc_obj.variables['longitude'][:])
print(nc_obj.variables['time'][:])
print(nc_obj.variables['temperature_anomaly'][:])
print(nc_obj.variables['field_status'][:])
lat = (nc_obj.variables['LAT'][:])
lon = (nc_obj.variables['LON'][:])
prcp = (nc_obj.variables['PRCP'][:])
print(lat)
print(lon)
print('---------------******-------------------')
print(prcp)



# calculate the mutual information index from the data of the valuable
from sklearn import metrics as mr
import math


def mutual_info(x, y):
    return mr.mutual_info_score(y, x)


# the code of model
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model


def cal(inputs):
    inputs = np.array(inputs)
    inputs = inputs / np.sum(inputs)
    W = [[0.28,   0.35, 0,   0.25,  0.11],
        [0.27,  0.3,   0.09,  0.12,  0.22],
        [0.21,  0.2,   0.23,  0.14,  0.23],
        [0.24, 0.09, 0.21, 0.13, 0.34],
        [0, 0.39, 0, 0.32, 0.29]]
    W = np.array(W)
    b = inputs.dot(W)  # 第三层的减少量
    We = [0.20, 0.35, 0.08, 0.16, 0.21]
    We = np.array(We)
    t = [x/w for x, w in zip(b, We)]
    result = sum(t)
    return result


# General a toy dataset:s it's just a straight line with some Gaussian noise:
xmin, xmax = -5, 5
n_samples = 100
np.random.seed(0)
X = np.random.normal(size=n_samples)
y = (X > 0).astype(np.float)
X[X > 0] *= 4
X += .3 * np.random.normal(size=n_samples)
X = X[:, np.newaxis]
clf = linear_model.LogisticRegression(C=1e5, solver='lbfgs')
clf.fit(X, y)
plt.clf()
X_test = np.linspace(0, 1.3)


def model1(x):
    return 1 / (1 + np.exp(-x))


loss = model(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, np.ones(shape=X_test.shape)*55.85/69, color='red', linewidth=1)
plt.plot(X_test, (loss+1)*460.1/69, color='green', linewidth=1)
plt.plot(X_test, (loss+1)*138.96/69, color='yellow', linewidth=1)
plt.plot(X_test, (loss+1)*32.10/69, color='blue', linewidth=1)

ols = linear_model.LinearRegression()
ols.fit(X, y)
plt.ylabel('Billion RMB/km^2/year')
plt.xlabel('Time Afterwards/year')
plt.xticks([0, 0.5, 1, 1.5, 2])
plt.yticks(range(0, 10))
plt.legend(('Economic Cost', 'Economic Profit', 'Ecosystem Service', 'Environment Cost'),
           loc="best", fontsize='small')
plt.show()


# calculate the ewm algorithm
import numpy as np
import pandas as pd
fp = "d:/code/tmp/data1.csv"
data = pd.read_csv(fp, index_col=None, header=None, encoding='utf8')
# data = (data - data.min())/(data.max() - data.min())
m, n = data.shape

data = data.as_matrix(columns=None)

k = 1/np.log(m)
yij = data.sum(axis=0)
pij = data/yij

test = pij*np.log(pij)
test = np.nan_to_num(test)
ej = -k*(test.sum(axis=0))

wi = (1-ej)/np.sum(1-ej)

print(wi)

