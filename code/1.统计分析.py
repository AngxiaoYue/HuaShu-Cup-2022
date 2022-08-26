import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

x_data = []
y_data = []

temp = []
f = open(r'data.txt', 'r')                   #以读方式打开文件
for line in f.readlines():                          #依次读取每行
    l = line.split('\t')
    l[-1] = l[-1].replace('\n', '')
    temp.append(l)

fig = plt.figure(figsize=(16, 13))
ax = fig.subplots(2, 3)    # 2*2

name = ['Thickness Analysis', 'Porosity Analysis', 'Compression Resilience Analysis', 'Filtration Resistance Analysis', 'Filtration Efficiency Analysis', 'Air Permeability Analysis',]
y_label = [r"$y1$", r"$y2$", r"$y3$", r"$w1$", r"$w2$", r"$w3$", ]
# 参数调整
for num in range(1, 7):
    for i in range(0, 25):
        x = (eval(temp[i * 2 + 1][-1]) - eval(temp[i * 2][-1]))
        y = (eval(temp[i * 2 + 1][num + 1]) - eval(temp[i * 2][num + 1])) / eval(temp[i * 2][num + 1]) * 100
        x_data.append(x)
        y_data.append(y)

    # 通过切片获取横坐标x1
    x1 = x_data
    # 通过切片获取纵坐标R
    y1 = y_data

    ax[int((num - 1) / 3), (num - 1) % 3].set_title(name[num-1])
    ax[int((num - 1) / 3), (num - 1) % 3].set_xlabel(r"$\alpha$" + ' (%)')
    ax[int((num - 1) / 3), (num - 1) % 3].set_ylabel(y_label[num-1] + ' (%)')
    if num < 4:
        ax[int((num - 1) / 3), (num - 1) % 3].scatter(x1, y1, marker=6, color='navy')
    else:
        ax[int((num - 1) / 3), (num - 1) % 3].scatter(x1, y1, marker='P', color='firebrick')

    x_data = []
    y_data = []

plt.show()
