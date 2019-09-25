# class DDQ:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# a = DDQ('abcde')
# for i in a:
#     print(i)
#生成器
# def SCQ(data):
#     for i in range(0,data,1):
#         yield i
# for j in SCQ(5):
#     print(j)
# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# sum(x*y for x,y in zip(xvec, yvec))

# class Mysxw:
#     def __init__(self,names):
#         self.names = names
#     def __enter__(self):
#         print('文件打开')
#         self.f = open(self.names,'r')
#         return self.f
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('文件关闭')
#         self.f.close()
#         print(exc_val)
#         return True
# with Mysxw("edg.txt") as f:
#     a = f.read()
#     print(1/0)
#     print(a)

# import contextlib
# @contextlib.contextmanager
# def myS(name):
#     print('打开')
#     f = open(name,'r')
#     yield f
#     print('关闭')
#     f.close()
# with myS('edg.txt') as f:
#     a = f.read()
#     print(a)

# class person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return '<person %s %s>'%(self.name,self.age)
# p = person("贾争",12)
# print(p)

# class ShortInputExcept:
#     def __init__(self,min,max):
#         self.min = min
#         self.max = max
#     def __str__(self):
#         return '字符串长度不足%s,当前为%s'%(self.min,self.max)
#
# name = input("请输入你的名字：")
# try:
#     if len(name)>2:
#         print('无此姓名')
#         raise ShortInputExcept(2,len(name))
# except ShortInputExcept as e:
#     print("超了")

# try:
#     num = input("输入一个数：")
#     print(num/0)
# except ValueError as v:
#     print(v)
# except ZeroDivisionError as z:
#     print(z)
# except TypeError as b:
#     print(b)
# else:
#     pass
# finally:
#     pass
for i in range(1,11):
    print(i)