from matplotlib import pyplot as plt
import random,matplotlib
from pylab import mpl


y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2= [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]


x = range(11,31)

plt.figure(figsize=(20,8),dpi=80)


mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False


#label 解释说明
plt.plot(x,y1,label="自己")
plt.plot(x,y2,label="同桌")

xtick = ["{}岁".format(i) for i in x]

#设置x轴
plt.xticks(x,xtick)

#设置y轴
plt.yticks(range(0,9))

#绘制网格 alpha=0.1用来设置透明度
plt.grid(alpha=0.1)

#添加图例
plt.legend()

plt.show()

















