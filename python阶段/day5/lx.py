# try:
#     f = open('a.txt','r',encoding='utf-8')
#     data = f.readlines()
#     print(data)
# finally:
#     print('异常')
# with open('a.txt','r') as f:
#     data = f.readlines()
#     print(data)
# import csv
# with open('b.csv','r+',newline="",encoding="utf-8") as f:
#     # write = csv.writer(f)
#     # for _ in range(0,10):
#     #     write.writerow(['a','b','c'])
#     # write.writerows([
#     #     ["a",'b','c'],
#     #     ["d",'e','f']
#     # ])
#     # reader = csv.reader(f)
#     # for row in reader:
#     #     print(row)
#     write = csv.DictWriter(f,['id','name','age'])
#     write.writeheader()
#     write.writerows([
#         {'id':'1','name':'xb','age':'12'}
#         {'id': '2', 'name': 'b', 'age': '12'}
#         {'id': '2', 'name': 'cb', 'age': '13'}
#     ])

