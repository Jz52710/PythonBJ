import os
# print(os.mkdir('a'))
# a = os.path.abspath('a') #返回文件或目录的绝对路径
# print(a)
# os.path.split('file_path') #将路径分割成目录和文件名，并用一个元组返回
# os.path.basename('path') #返回路径最后的文件名，如果后面还有\/那么返回一个空字符串。
# os.path.exists('file_path') #如果路径存在，则返回True,繁殖返回False
# os.path.join('file_path','file_name') #路径拼接

# a = os.path.isdir('a') #判断是否为目录
# b = os.path.isdir('week.py')
# print(a)
# print(b)
# c = os.path.isfile('a') #判断是否为文件
# d = os.path.isfile('jz.py')
# print(c)
# print(d)
# e = os.path.islink('a') #判断是否是链接
# # f = os.path.islink('https://movie.douban.com/top250')
# print(e)
# print(f)
# g = os.path.getsize('dist') #返回文件大小，如果文件不存在，就返回错误。
# print(g)