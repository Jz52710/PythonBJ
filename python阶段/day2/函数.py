# def fn(a,b):
#     return a+b
# a=fn(1,2)
# print(a)

# def fn(a,b=20):
#     return a+b
# a=fn(10)
# print(a)

# def fn(*args):
#     print(args)
# fn(1,2,2,3,4,5,6,7)

# def fn(**kwargs):
#     print(kwargs)
# fn(a=1,b=2)

# def fn(a,b,c):
#     print(a,b,c)
# t = [10,20,30]
# fn(*t)
# fn('xx',12)
# b={'name':'xx','age':12}
# fn(**b)

# def fn(a,c):
#     print(a,c)
# # fn('xx',12)
# b = {'a':'xx','c':12}
# fn(**b)

# def fn():
#     return 1,2,3,4,5
# a = fn()
# print(a)
# a,b,c,d,e = fn()
# print(a,b,c,d,e)

# def fn():
#     arr = []
#     def Newfn(a):
#         arr.append(a)
#         print(arr)
#     return Newfn
# a = fn()
# a(1)
# a(2)

# def fn(num):
#     if num==1:
#         return 1
#     else:
#         return num*fn(num-1)
# a=fn(3)
# print(a)

# def fn(num):
#     return  1  if num==1 else num*fn(num-1)
# a = fn(3)
# print(a)

# def fn(a):
#     def fn1(b):
#         def fn2(c):
#             return a+b+c
#         return fn2
#     return fn1
# a = fn(1)(2)(3)
# print(a)

# import time
#
# def fn():
#     time.sleep(1)
#     print("hello world")
#
# def fn1():
#     time.sleep(1)
#     print("hello")
#
# def fn2(fn):
#     def newFn():
#         start = time.time()
#         fn()
#         end = time.time()
#         print(f"总时间为：{end-start}")
#     return newFn
#
# # fn2(fn1)()
# # fn2(fn)()
# fn = fn2(fn)
# fn1 = fn2(fn1)
#
# fn()
# fn1()

# staus = 0 #0是未登录 1是登录
# def login():
#     global staus
#     username = input("请输入用户名：")
#     passwd = input("请输入密码：")
#     if username=='jz' and passwd=='52710':
#         staus =1
#         print("登录成功")
#     else:
#         print("登录失败")
#
# def logOn(fn):
#     def newFn(*args,**kwargs):
#         if staus==1:
#             fn(*args,**kwargs)
#         else:
#             login()
#     return newFn
#
# @logOn
# def fn1(id):
#     print("成绩查看页面%s"%id)
# @logOn
# def fn2(id):
#     print("课程查看页面%s"%id)
#
# login()
# d={'jz':77,'chf':88,'qyt':100}
# fn1(d['jz'])
# fn2(100)

# import time
#
# def xs(type):
#     def newXs1(fn):
#         def newXs(*args,**kwargs):
#             start =time.time()
#             end = time.time()
#             if type==0:
#                 fn(*args,**kwargs)
#                 end = time.time()
#                 print(f"总时间：{end - start}")
#             elif type==1:
#                 fn(*args, **kwargs)
#                 print(f"开始时间：{start}")
#             elif type==2:
#                 fn(*args, **kwargs)
#                 print(f"结束时间：{end}")
#         return newXs
#     return newXs1
#
# @xs(2)
# def fn(a):
#     time.sleep(1)
#     print(a)
#
# fn("我丢丢我")

# name = "小白"
# def fn():
#     global name
#     name = "小红"
#     print(name)  # 小红
#     def newFn():
#         global name
#         # nonlocal name
#         name = "小黑"
#         print(name) # 小黑
#     newFn()
#     print(name)
#
# fn()
# print(name)  # 小白

# import time
#
# def ct1(fn):
#     def newCt(*args,**kwargs):
#         fn(*args, **kwargs)
#         end = time.time()
#         print(f"结束时间：{end}")
#     return newCt
# def ct(fn):
#     def newCt(*args,**kwargs):
#         start = time.time()
#         fn(*args, **kwargs)
#         print(f"开始时间：{start}")
#     return newCt
# @ct1
# @ct
# def fn(a):
#     time.sleep(1)
#     print(a)
#
# fn("hell")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}=%2d '%(i*j),end="")
#     print("")

# print("\n".join([ "".join([ f'{j}*{i}=%2d '%(i*j) for j in range(1,i+1)]) for i in range(1,10)]))

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print("")

# print("\n".join([ "".join(["*" for j in range(1,i+1)]) for i in range(1,6)]))

# for i in range(1,6):
#     con = ""
#     for j in range(1,i):
#         con+=" "
#     for k in range(1,7-i):
#         con+="*"
#     print(con)

# print([["*" for j in range(6,i)] for i in range(6,1) ])

# d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'A':['a','b','c'],'B':['a']}
# d2 = {k+"1":v+['a'] for k,v in d1.items()}
# print(d2)

# d1 = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'A':['a','b','c'],'B':['a']}
# d2 = {k.lower():d1.get(k.lower(),[])+d1.get(k.upper(),[]) for k,v in d1.items()}
# # d2 = {k.lower():v for k,v in d1.items() if k in ['a','b','c']}
# print(d2)