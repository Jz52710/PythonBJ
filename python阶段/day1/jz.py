#单行注释
'''

'''
"""
多行注释
语法特点：
严格遵循缩进原则，不要轻易使用空格
"""
# input("输入一个数：")
# print(12+12)
# name = "jz"
# print(name,123,123+123)
# a=b=c='aaaa'
# d='开始了'
# e,f,g='1',"2","3"
# print(b)
# print(d)
# print(e,f,g)
# name = "贾争"
# print(f"我是{name},我有%d个形态"%2,"我价值%0.2f亿美金"%10)
# str = '我是博学多才小王子'
# print(str[2:6:1])
# print(str[-1:-4:-1])
# print(str[-7:-3])
# print(f"我是%s，欢迎来到%s，装备有%d套，价值%0.2f亿"%("渣渣辉","贪玩蓝月",10,500))
# arr=[]
# arr.append("abc") #末尾添加
# arr.insert(0,"qqw") #在第几位添加
# arr.insert(1,"111")
# print(arr)
# arr = [1,2,3]
# print(arr[0])
# arr.remove(1)#移除1
# arr.pop(0) #下标
# arr.clear()
# del arr[1]
# print(arr)
# print(dir(str))
# print(dir(list))
# print(dir())
# d1 = {'name':'qq','age':12,'sex':'男'}
# d1.update('edg'123)
# d1.pop("name")
# d1.popitem()
# del d1['age']
# d1.clear()

# d1['edg'] = 'clearlove'
# d1.update({'edg':'iboy'})

# d1['name']='abc'
# print(d1)

# print(d1.get('a',"无"))
# print(d1['name'])

# print(dir(tuple))
# s = {1,2,3,4,5}
# s.update({7,8,9})#{1, 2, 3, 4, 5, 7, 8, 9}
# s.update("abc")#{1, 2, 3, 4, 5, 'c', 'a', 'b'}
# s.update(["aa","bb"])#{1, 2, 3, 4, 5, 'bb', 'aa'}
# s.add("jz")
# print(s)

# s.pop()#{2, 3, 4, 5}
# s.remove(4)#{1,2, 3, 5}
# s.clear()#set()
# print(s)

# s1 = {6,7,8,1,2}
# print(s&s1)#{1, 2}
# print(s|s1)#{1, 2, 3, 4, 5, 6, 7, 8}
# print(s^s1)#{3, 4, 5, 6, 7, 8}

# print('123'+'123')
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))

# print("123"*3)
# print([1,2,3]*3)
# print((1,2,3)*3)

# print(12//5)

# print(2**10)

# print(1 in [1,2,3])#True
# print(1 not in [1,2,3])#False

# name = "jz"
# name1 = "jz"
# print(name is name1)
# print(name is not name1)

# print("1>2") if 1>2 else print("2>1")

# a=2
# a**=10
# print(a)

# for i in range(0,10):
#     print(i)
# else:
#     print("GG")

# for i in range(0,10):
#     print(i)
#     if i==5:
#         break
# else:
#     print("G")
# a = 1.1
# print(int(a))

# a = 1
# print(float(a))

# a = range(0,10)
# print(tuple(a))

# a = ["12","bb"]
# print(dict(a))

# a="aa"
# print(str(a))

# 1.操场上100多人排队，三人一组多1人，四人一组多2人，五人一组多3人，共多少人？(118，178)
# for i in range(100,200):
#     if i%3==1 and i%4==2 and i%5==3:
#         print(i)
# 2.从1到500所有自然数中不含数字4的自然数共有多少个？（324）
# sum = 0
# for a in range(0,5):
#     for b in range(0,10):
#         for c in range(0,10):
#             if a!=4 and b!=4 and c!=4:
#                 sum+=1
# print(sum)
# 3.一个四位数，恰好等于去掉它的首位数字之后所剩的三位数的3倍，这个四位数是多少？
# for n in range(0,9999):
#     sum=n%1000
#     if sum==n/3:
#         print(n)
# 4.两个自然数X，Y相除，商3余10，被除数、除数、商、余数的和是163，求被除数、除数。 (115、35)
# for x in range(0,150):
#     y=(x-10)/3
#     if x+y==150:
#         print(x,y)
# 5.某数学竞赛中，参赛人数大约在380~450人之间。比赛结果，全体考生的总平均分为76分，男生的平均分为75分，女生的平均分为80.1分，求男女生各有多少人？(328，80)
# for i in range(0,450):
#     for j in range(0,450):
#         if i+j>380 and i+j<450:
#             if i*75+j*80.1==(i+j)*76:
#                 print(i,j)
# 6.有一个两位数，如果在它的前面添一个3，可得到一个三位数；把3添在它的后面，也可以得到一个三位数。这两个三位数相差468，求原来的两位数。（85）
# for sum in range(10,100):
#     if sum+300==sum*10+3-468:
#         print(sum)
# 7.某人去购买教材和练习簿。已知教材每本10元，教参每本5元，练习簿每本0。5元，他总共购买了100本，用了100元。问他购买教材、教参和练习簿各多少本？（1、9、90）
# for i in range(1,10):
#     for j in range(1,20):
#         for m in range(1,200):
#             if 10*i+5*j+0.5*m==100 and i+j+m==100:
#                 print(i,j,m)
# 8.将100元纸币兑换成10元、5元和1元纸币共20张，输出各种兑换法，并统计个数。（4、11，5；8、2、10；S=2）
# for a in range(1,10):
#     for b in range(1,20):
#         for c in range(1,200):
#             if 10*a+5*b+1*c==100 and a+b+c==20:
#                 print(a,b,c)
# 9.有红、白、黑三种球若干个，其中红、白球共25个，白、黑球共31个，红、黑球共28个，求这三种球各多少个？（11、14、17）
# for m in range(1,25):
#     for n in range(1,25):
#         if m+n==25:
#             for i in range(1,31):
#                 if m+i==31 and n+i==28:
#                     print(m,n,i)
# 10.甲、乙、丙、丁四人共加工零件370个，如果把甲做的个数加10个，乙做的个数减20个，丙做的个数乘以2，丁做的个数除以2，四人做的零件数正好相等，求甲实际加工了多少个零件？(70)
# for i in range(1,370):
#     j=i+10+20
#     n=(i+10)/2
#     m=(i+10)*2
#     if i+m+j+n==370:
#         print(i)
# 11.一个六位自然数，将其末位上数字7移至首位，其余数字依次向右移动一位，得到一个新的六位数，新的六位数是原六位数的4倍，求原数。 (179487)
# for i in range(10000,100000):
#     n=i*10+7
#     m=7*100000+i
#     if m==4*n:
#         print(n)
# 12.要在[ ]、[ ]7、[ ]48这三个数中的每个[ ]内各填上1~9中的一个数字，使中间的两位数是左边的一位数和右边的三位数的平均数，求这三个数。（6、77、148）
# for i in range(1,9):
#     for j in range(1,9):
#         for m in range(1,9):
#             if j*10+7==((i+m*100+48)/2):
#                 print(i,j*10+7,m*100+48)
# 13.输出四位自然数中各位数字之和为6并且各位数字互不相同的数，并统计个数。（1023、1032、1203、1230、1302、1320、……、3201、3210，18）
# num=0
# for a in range(1,10):
#     for b in range(0,10):
#         if b==a:
#             continue
#         for c in range(0,10):
#             if c==b:
#                 continue
#             for d in range(0,10):
#                 if d==c:
#                     continue
#                 if a+b+c+d==6:
#                     num+=1
#                     print(a*1000+b*100+c*10+d)
# print(num)
# 14.由数字1、2、3、4、5、6六个数字共可组成多少个没有重复数字的四位数，输出这些数据并统计个数。（1234、1235、1236、1243、1245、1246、1253、……、6542、6543，S=360）
# num=0
# for a in range(1,7):
#     for b in range(1,7):
#         for c in range(1,7):
#             for d in range(1,7):
#                 if a!=b and a!=c and a!=d and b!=d and b!=c and c!=d:
#                     print(a*1000+b*100+c*10+d)
#                     num+=1
# print(num)
# 15.打印“＊”字三角形：从键盘输入一个自然数Ｎ（１《Ｎ《 ９）。根据Ｎ的值，打印输出对应的“＊”字三角形。如Ｎ＝４，输出
# for i in range(0,4):
#     str=""
#     for k in range(0,4-i-1):
#         str+=" "
#     for j in range(0,2*(i+1)-1):
#         str+="*"
#     print(str)
# arr=['Google', 'Runoob', 'Taobao', 'Facebook']
# arr.append("aa")
# arr1=[7,8,9]
# arr.extend(arr1)
# arr.insert(1,"aa")
# arr.clear()
# arr.pop()
# arr.remove(3)
# print(arr.count(1))
# print(arr)
# print(arr.index(3))
# print(arr.reverse())
# arr.sort()
# print(arr)
# arr=['e', 'a', 'u', 'o', 'i']
# arr.sort(reverse=True)
# print(arr)
# arr=[1,2,3,4,5,6]
# print(arr.copy())
# t = (1,2,3,4,5,6,3,3,3)
# print(t.index(3))
# print(t.count(3))

# str="abcdefgg"
# print(str.capitalize())
# print(str.center(20))
# print(str.center(20,"_"))
# print(str.count('g',2,7))
# str = "我开始了"
# str1 = str.encode('base64', 'strict')
# print(str.encode('UTF-8', 'strict'))
# print("Encoded String: " + str)
# print("Decoded String: " + str.decode('base64', 'strict'))
# str =b'\xe6\x88\x91\xe5\xbc\x80\xe5\xa7\x8b\xe4\xba\x86'
# print(str.decode('UTF-8', 'strict'))
# str ='abcdefffe'
# print(str.endswith('e'))
# print(str.endswith('e',1))
# print(str.endswith('e',1,3))
# str='a\tb\tc'
# print(str)
# # print(str.expandtabs(tabsize=8))
# str="abcdefg"
# print(str.index('f'))
# print(str.index('f',1,4))
# str="12ab/"
# # print(str.isalnum())
# str=''
# print(str.isalpha())
# str='abc'
# print(str.islower())
# str = '123'
# print(str.isnumeric())
# str=' '
# print(str.isspace())
# str='We Are One'
# print(str.istitle())
# str='EABC'
# print(str.isupper())#True
# str='abc'
# print(str.isupper())#False
# str = "-"
# seq = ("a", "b", "c") # 字符串序列
# print(str.join( seq ))
# str = '123abcd'
# print(len(str))
# str='123qwe'
# print(str.ljust(10,'0'))
# str='ABC'
# print(str.lower())
# str='AaBbCc'
# print(str.swapcase())
# str='123a'
# print(str.lstrip('1'))
# str="this is string example....wow!!!"
# intab = "ab"
# outtab = "12"
# print(str.maketrans(intab,outtab))
# str='abcdeeefd'
# print(str.replace('d','a'))
# print(str.replace('e','b',2))
# str='abcdef'
# print(str.rfind('e'))
# print(str.rfind("e",1,4))
# str='abcdef'
# print(str.rindex('e'))
# print(str.rindex('e',1,4))
# str='abcdef'
# print(str.rjust(10))
# print(str.rjust(10,'0'))
# str='abcd   '
# print(str.rstrip())
# str='a b c'
# print(str.rsplit( ))
# print(str.rsplit(' ',1))
# str1 = 'ab c\n\nde fg\rkl\r\n'
# print(str1.splitlines())
# print(str1.splitlines(True))
# str='abcd'
# print(str.startswith('a'))
# print(str.startswith('a',2,4))
# str='          abcde       '
# print(str.strip(' '))
# str='Are You OK?'
# print(str.title())
# intab = "aeiou"
# outtab = "12345"
# trantab =str.maketrans(intab, outtab)
# str = "this is string example....wow!!!";
# print(str.translate(trantab))
# print(str.translate(trantab,'xm'))
# str='123abc'
# print(str.zfill(6))
# print(str.zfill(10))
str='123a'
print(str.isdecimal())