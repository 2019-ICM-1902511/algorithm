import numpy as np
import csv


class AHP:
    def __init__(self, array):
        self.row = len(array)  # 计算矩阵的行数
        self.col = len(array[0])  # 计算矩阵的列数
        self.array = array

    def get_tezheng(self, array):  # 获取最大特征值和对应的特征向量
        te_val, te_vector = np.linalg.eig(array)  # numpy.linalg.eig() 计算矩阵特征值与特征向量
        list1 = list(te_val)  # te_val是一个一行三列的矩阵，此处将矩阵转化为列表
        print("特征值为：", te_val)
        print("特征向量为：", te_vector)

        # 得到最大特征值对应的特征向量
        max_val = np.max(list1)  # 最大特征值
        index = list1.index(max_val)  # 最大特征值在列表中的位置
        max_vector = te_vector[:, index]  # 通过位置来确定最大特征值对应的特征向量
        print("最大的特征值:"+str(max_val)+"   对应的特征向量为："+str(max_vector))
        return max_val, max_vector

    def RImatrix(self, n):  # 建立RI矩阵，该矩阵是AHP中自带的，类似标杆一样，除n之外的值不能更改
            d = {}
            n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            n2 = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45]
            for i in range(n):  # 获取n阶矩阵对应的RI值
                d[n1[n]] = n2[n]
            print("该矩阵在一致性检测时采用的RI值为：", d[n1[n]])
            return d[n1[n]]

    def test_consitstence(self, max_val, RI):  # 测试一致性，AHP中最重要的一步，用于检验判断矩阵中的数据是否自相矛盾
            CI = (max_val-self.row)/(self.row-1)  # AHP中计算CI的标准公式
            CR = CI/RI  # AHP中计算CR的标准公式
            if CR < 0.10:
                print("判断矩阵的CR值为  " + str(CR) + "通过一致性检验")
                return True
            else:
                print("判断矩阵的CR值为  " + str(CR) + "判断矩阵未通过一致性检验，请重新输入判断矩阵")
                return False  

    def normalize_vector(self, max_vector):  # 特征向量归一化
            vector_after_normalization = []  # 生成一个空白列表，用于存放归一化之后的特征向量的值
            sum0 = np.sum(max_vector)  # 将特征向量的每一个元素相加取和
            for i in range(len(max_vector)):
                # 将特征向量的每一个元素除以和，得到比值，保证向量的每一个元素都在0和1之间，直线归一化
                # 将归一化之后的元素依次插入空白列表的尾部
                vector_after_normalization.append((max_vector[i]/sum0))

            print("该级指标的权重矩阵为：  " + str(vector_after_normalization))
            return vector_after_normalization

    def weightCalculator(self, normalMatrix):  # 计算最终指标对应的权重值
        # layers weight calculations.
        listlen = len(normalMatrix) - 1  # 设置listlen的初始值为normalMatrix最后一个元素的index
        layerWeights = list()  # 空白权重列表
        while listlen > -1:
            sum = float()  # sum的初始值为0.0，并且限制了sum的类型为浮点型
            for i in normalMatrix:
                sum += i[listlen]  # 求normalMatrix各元素的和
            sumAverage = round(sum / len(normalMatrix), 3)  # 求normalMatrix各元素的平均值，并保留三位小数
            layerWeights.append(sumAverage)  # 为什么平均值是权重？？？？？？
            listlen -= 1
        return layerWeights


class AHP_method:
    def __init__(self, path: str):
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
        weigh_matrix = []
        for i in self.arrays:
            print(i)
            a = AHP(i)
            max_val, max_vector = a.get_tezheng(i)
            record_max_vector = max_vector
            RI = a.RImatrix(len(i))
            flag = a.test_consitstence(max_val, RI)
            while not flag:
                print("对比矩阵未通过一致性检验，请重新输入对比矩阵！")
                break
                # flag = to_input_matrix(length)
            weight = a.normalize_vector(record_max_vector)  # 返回权重[[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]
            weigh_matrix.append(weight)
        print("最终的权重矩阵为：", weigh_matrix)
        return weigh_matrix


if __name__ == "__main__":
    path = "D://code//ICM//algorithms//data//ahp1.csv"
    method = AHP_method(path)
    result = method.test_consitstence()
    w0 = result[0]
    w = result[1:]
    w0 = np.array(w0)
    w = np.array(w)
    res = w0.dot(w)
    print(res)
