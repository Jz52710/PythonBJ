import math
import random
import time
import os
import calendar
# a = -1
# print(abs(a))
#
# a = 1.4
# print(math.ceil(a))
#
# a = 2
# print(math.exp(a))

# a = -2
# print(math.fabs(a))
#
# a = 1.4
# print(math.floor(a))

# a = math.e
# print(math.log(a))
# print(math.log(100,10))

# a = 10
# print(math.log10(a))

# a = ['1','2','3']
# print(max(a))
#
# a = ['1','2','3']
# print(min(a))

# a = 111.777
# print(math.modf(a))

# a = 2
# b = 2
# print(pow(a,b))

# a = 77.777888
# print(round(a))
# print(round(a,2))

# a = 4
# print(math.sqrt(a))

# a = range(0,10)
# print(random.choice(a))

# print(random.randrange(1,100,2))
# print(random.randrange(100))

# print(random.random())

# random.seed()
# print(random.random())
#
# random.seed(20)
# print(random.random())
#
# random.seed('hello',2)
# print(random.random())

# a = [1,2,3,4,5]
# print(random.shuffle(a))

# list = [20, 16, 10, 5];
# random.shuffle(list)
# print (list)

# print(random.uniform(1,10))

# print(math.acos(1))
# print(math.acos(0.64))

# print(math.asin(1))
# print(math.asin(0))

# print(math.atan(1))
# print(math.atan(0))

# print(math.atan2(5,5))

# print(math.cos(math.pi))
# print(math.cos(0))

# print(math.sin(math.pi/2))
# print(math.sin(0))
#
# print(math.tan(math.pi/2))
# print(math.tan(0))

# print(math.hypot(0,2))
# print(math.hypot(3,2))

# print(math.degrees(math.pi/2))
# print(math.degrees(math.pi/4))

# print(math.radians(90))
# print(math.radians(30))
# print(math.radians(60))
# print(math.radians(45))
# print(math.radians(180))

# d1 = {'name':'jz','age':20,'sex':'男'}
# dict.clear(d1)
# d2 = d1.copy()
# a = ['a','b','c']
# d2 = dict.fromkeys(a,1)
# print(d2)
# if 'name' in d1:
#     print('name键在')
# else:
#     print('name键不在')
# print('edg' in d1)
# for k,v in d1.items():
#     print(k,v)
# for k in d1.keys():
#     print(k)
# d1.setdefault('edg',7777)
# print(d1)
# a = d1.setdefault('name')
# print(a)
# d2 = {'edg':77777,'rng':'mlxg'}
# d1.update(d2)
# print(list(d1.values()))
# d1.pop('age')
# print(d1)
# d1.popitem()
# print(d1.popitem())
# print(d1)

# print(dir(time))
# print(time.altzone)
# t = time.localtime()
# print(time.asctime(t))
# def fn():
#     time.sleep(1)
#
# start = time.clock()
# fn()
# end = time.clock()
# print(f'{end-start}')
#
# start1 = time.time()
# fn()
# end1 = time.time()
# print(f'{end1-start1}')
# t = time.gmtime()
# print(time.asctime(t))

# t1 = ['2018','5','27','1','5','27']
# print(time.asctime(t1))

# print(time.ctime())
# print(time.gmtime())
# print(time.localtime())
# print(time.mktime())
# t = (2020, 6, 6, 7, 7, 7, 1, 48, 0)
# print(time.asctime(t))
# secs = time.mktime(t)
# print(secs)
# print(time.asctime(time.localtime(secs)))

# def fn():
#     time.sleep(7)
#
# fn()
# print('推迟7秒')

# print(time.strftime())
# t = (2020, 2, 17, 17, 3, 38, 1, 48, 0)
# t1 = time.mktime(t)
# print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t1)))

# t = time.strptime("30 Sep 20", "%d %b %y")
# print(t)
#
# os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
# time.tzset()
# print(time.strftime('%X %x %Z'))

# print(dir(time))
# print(time.tzname)
# print(time.timezone)
# print(time.daylight)

# print(dir(calendar))
# print(calendar.calendar(2019))
# print(calendar.firstweekday())
# print(calendar.isleap(2019))
# print(calendar.isleap(2020))
# print(calendar.leapdays(2015,2021))
# print(calendar.month(2019,9))
# print(calendar.monthrange(2019,9))
# print(calendar.prcal(2019))
# print(calendar.prmonth(2019,9))
# calendar.setfirstweekday(6)
# print(calendar.month(2019,9))
# print(calendar.timegm())
# print(calendar.weekday(2019,9,4))
# print(calendar.timegm(time.localtime()))

jh = {'a','b','c'}
# jh.add('jz')
# jh.clear()
# jh1 = jh.copy()
# jh1 = {'a','b','d'}
# jh2 = jh.difference(jh1)
# jh.difference_update(jh1)
# jh.discard('a')
# jh2 = jh.intersection(jh1)
# jh.intersection_update(jh1)
# print(jh.isdisjoint(jh1))
# print(jh)
# jh = {'a','b','c'}
jh1 = {'jz','777'}
# print(jh.isdisjoint(jh1))#False
# jh2 = jh.issubset(jh1)
# jh2 = jh.issuperset(jh1)
# jh.pop()
# jh.remove('b')
# jh2 = jh.symmetric_difference(jh1)
# jh.symmetric_difference_update(jh1)
# jh2 = jh.union(jh1)
jh.update(jh1)
print(jh)