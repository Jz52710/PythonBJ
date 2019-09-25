import numpy as np
np.set_printoptions(threshold=np.inf)
data = np.loadtxt('mpg.txt',skiprows=1,usecols=range(6))
# print(data)
y = data[:,:1]
x = data[:,1:]
# print(y)
# print(x)
mean = np.mean(x,axis=0)#平均值
# print(mean)
std=np.std(x,axis=0)#标准差
# print(std)
res=(x-mean)/std#标准化处理
# print(res)

#测试数据
testdata=[8,307.0,130.0,3504,12.0]
testdata=(testdata-mean)/std
diff=res-testdata
disstance=np.sum(diff**2,axis=1)
sortarr=np.argsort(disstance)#返回排序后的下标
# print(sortarr)
# print(y)
resdate={}#字典
for i in range(10):
    cla=y[sortarr[i]][0]
    resdate.setdefault(cla,0)
    resdate[cla]+=1
print(resdate)
print(sorted(resdate,key=lambda x:resdate[cla])[0])#排序