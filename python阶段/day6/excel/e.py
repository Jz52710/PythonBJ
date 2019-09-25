from datetime import datetime
import time
# open(datetime.now().date().strftime('%Y-%m-%d %H:%M:%S')+'.txt', 'w').close()
# print(time.strftime())
# print(time.strftime(time.localtime(time.time())))
# print(time.time())
# print()
# t = str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
# print(t)
# open(datetime.now().date().strftime('%Y-%m-%d %H:%M:%S')+'.txt', 'w').close()
#encoding:utf-8
import os,sys
# import csv
# import time
#
#
# now = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
# fname=now+".xls"
# csvFile = open(fname,'wb')
#
#
#
# fileHeader = ["x", "y","z"]
# writer = csv.writer(csvFile)
# writer.writerow(fileHeader)
#
#
# csvFile.close()
from collections import deque
d =deque(maxlen=20)
for i in range(30):
    d.append(str(i))
print(d)