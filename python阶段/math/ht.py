import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import  Axes3D
fig=plt.figure()
# plt.plot([1,2,3],[4,5,6],linewidth=2,color='SkyBlue',)
# plt.plot([1,2,3],[4,5,6],'r--*')
# plt.xlabel('嗡嗡嗡')
# plt.ylabel('y')
# plt.xlim(0,10)
# plt.ylim(0,10)
# plt.title("一根藤-")
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# # plt.rcParams['axes.unicode_minus']=False
# plt.xticks(np.linspace(1,10,4),["tom","名字","age","男"])
# plt.annotate('气球',xy=(4,4))
# plt.annotate('葫芦',xy=(2.5,4),xytext=(4,8),arrowprops=dict(facecolor='pink'))
# plt.grid(True)
# ax=plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# print(dir(ax.spines))
# plt.ylim(0,50)
# x = np.arange(1,10)
# y1=[5 for i in x]
# plt.plot(x,y1,label='直线')
#
# y2=[i**2 for i in x]
# plt.plot(x,y2,label='二次')
#
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# y3=[2**i for i in x]
# plt.plot(x,y3,label='指数函数')
#
# y4=[2*i+5 for i in x]
# plt.plot(x,y4,label='一次函数')
#
# y5=[np.log(i) for i in x]
# plt.plot(x,y5,label='对数函数')
# x1 = np.random.randn(1000)
# y=np.random.randn(1000)
# plt.scatter(x1,y,marker='.')

# x = np.arange(1,10)
# y1=[i**2 for i in x]
# plt.bar(x,y1)
# plt.hist(x,y1)
# plt.pie(x)
# plt.boxplot(np.arange(-4,4))
# df['我'].plot(kind='bar')
# df['五年'].plot(kind='hist')
# plt.rcParams['font.sans-serif']=['Microsoft YaHei']
# plt.legend(loc='best')
# plt.show()
# import math
#
# u = 0  # 均值μ
# #u01 = -2
# sig = math.sqrt(1)  # 标准差δ
#
# x = np.linspace(u - 3 * sig, u + 3 * sig, 50)
# y_sig = np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (math.sqrt(2 * math.pi) * sig)
# plt.plot(x, y_sig, "r-", linewidth=2)
# plt.grid(True)
# plt.show()
#3D
fig=plt.figure()
fig1=Axes3D(fig)
z=np.linspace(1,13,1000)
x=np.sin(z)
y=np.cos(z)
fig1.plot3D(x,y,z)

z1=np.random.uniform(1,13,100)
print(z1)
x1=np.sin(z1)
y1=np.cos(z1)
fig1.scatter3D(x1,y1,z1,edgecolors='r')

plt.show()