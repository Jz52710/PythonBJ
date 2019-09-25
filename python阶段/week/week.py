from sys import argv
import xlwt
import time
from collections import deque
#打开txt
list1 =[]
with open('data.txt','r',encoding='utf-8') as f:
    data = f.readline()
    for i in data:
        a = data.split()
        list1.append(a)
        data = f.readline()
#时间
t = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
#读
# book = xlwt.Workbook()
# mysheel = book.add_sheet('time')
# lenght = len(list1)
# for i in range(0,lenght):
#     a = list1[i][0]
#     b = list1[i][1]
#     c = list1[i][2]
#     mysheel.write(i,0,a)
#     mysheel.write(i,1,b)
#     mysheel.write(i,2,c)
# # d = deque(maxlen=3)
# book.save(t+'.xls')
# # print(d)