# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
fp = "d:/code/tmp/data1.csv"
data = pd.read_csv(fp, index_col=None, header=None, encoding='utf8')
# data = (data - data.min())/(data.max() - data.min())
m, n = data.shape
# 第一步读取文件，如果未标准化，则标准化
data = data.as_matrix(columns=None)
# 将dataframe格式转化为matrix格式
k = 1/np.log(m)
yij = data.sum(axis=0)
pij = data/yij
# 第二步，计算pij
test = pij*np.log(pij)
test = np.nan_to_num(test)
ej = -k*(test.sum(axis=0))
# 计算每种指标的信息熵
wi = (1-ej)/np.sum(1-ej)
# 计算每种指标的权重
print(wi)