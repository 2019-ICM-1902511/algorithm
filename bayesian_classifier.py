# 高斯朴素贝叶斯

import numpy as np
from sklearn.naive_bayes import GaussianNB
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB().fit(X, Y)
print(clf.predict([[-0.8, -1]]))
'''
partial_fit说明：增量的训练一批样本
这种方法被称为连续几次在不同的数据集，从而实现核心和在线学习，这是特别有用的，当数据集很大的时候，不适合在内存中运算
该方法具有一定的性能和数值稳定性的开销，因此最好是作用在尽可能大的数据块（只要符合内存的预算开销）
'''
clf_pf = GaussianNB().partial_fit(X, Y, np.unique(Y))
print(clf_pf.predict([[-0.8, -1]]))
