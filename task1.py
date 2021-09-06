from sklearn.datasets import make_circles
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1)
X, Y = make_circles(n_samples=400,shuffle=True, noise=0.05, factor=0.5)
plt.subplot(121)
plt.title('make_circles function example')
plt.scatter(X[:, 0], X[:, 1], marker='*', c=Y)
plt.show()
#参数说明
# n_samples：整数 可选 默认为100
# 生成的总点数。（如果是奇数，内圆比外圆多一点，但是测试输入5后，内圆和外圆均是两个点）
#
# shuffle：布尔变量 可选 默认为True
# 是否打乱样本
#
# noise：double 或None  默认为None
# 将高斯噪声的标准差加入到数据中
#
# random_state：整数 RandomState instance or None
# 确定数据集变换和噪声的随机数生成。
#
# factor：0 < double < 1 默认值0.8
# 内外圆之间的比例因子

fig = plt.figure(1)
X, Y = make_circles(n_samples=400,shuffle=True, noise=0.05, factor=0.5)
plt.subplot(121)
plt.title('data by make circles()')
plt.scatter(X[:, 0], X[:, 1], marker='*', c=Y,cmap='coolwarm')

X, Y = make_moons(n_samples=400,shuffle=True, noise=0.05)
plt.subplot(122)
plt.title('data by make moons()')
plt.scatter(X[:, 0], X[:, 1], marker='+', c=Y,cmap='Oranges')
plt.show()