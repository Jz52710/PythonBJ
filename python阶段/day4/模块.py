# print(__name__)
# import jz
# from jz import *
# import sys
# print(sys.argv)
# jz.jf(1,2,3,4)
# jz.cp('qwe')
# jf(1,2,3,4)
# cp('a')
# jf(5,6,7)
# from qyt import *
# qyt.jf(1,2,3)
from sys import argv
# print([int(i) for i in argv[1:]])
fobj = open('a.txt','w')
fobj.write('hello')
fobj.close()
fobj = open('a.txt','rb')
a=fobj.read(3)
print(a)
print(fobj.tell())
fobj.seek(0,1)
print(a)
print(fobj.tell())
fobj.close()
# fobj = open('a.txt','rb+')
# fobj.seek(a,0)
