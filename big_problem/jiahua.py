import read_data
import numpy as np

data = read_data.read_data()
tmp = []
for i in range(data.shape[0]):
    if i % 10 == 0:
        tmp.append(data[i])
        
print(tmp)
    
np.savetxt('jiahua.csv', tmp, delimiter=',')
