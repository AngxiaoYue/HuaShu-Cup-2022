import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


data = pd.read_excel('data.xlsx')


# 提取变量名
label_need = data.keys()[0:]

# 提取上面变量名下的数据
data1 = data[label_need].values

# 数据归一化
[m, n] = data1.shape
data2 = data1.astype('float')
data3 = data2

ymin = 0.002
ymax = 1

for j in range(0,n):
    d_max = max(data2[:, j])
    d_min = min(data2[:, j])
    data3[:, j] = (ymax - ymin) * (data2[:, j] - d_min) / (d_max - d_min) + ymin

# 得到其他列和参考列相等的绝对值
for i in range(0, 9):
    data3[:, i] = np.abs(data3[:, i] - data3[:, 7])

#得到绝对值矩阵的全局最大值和最小值
data4 = data3[:, 0:9]
d_max = np.max(data2)
d_min = np.min(data2)
a = 0.5 #定义分辨系数

# 计算灰色关联矩阵
data4 = (d_min + a * d_max) / (data4 + a * d_max)
xishu = np.mean(data4, axis=0)
print('灰色关联度结果分别为：')
print(xishu)
