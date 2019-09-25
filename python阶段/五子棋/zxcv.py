from random import randint

size = int(input("请输入棋盘大小:\n"))
arr = []

# 初始化棋盘
def init():
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append("口")
    # print(arr)
init()

# 绘制棋盘
def draw():
    for i in arr:
        for j in arr[arr.index(i)]:
            print(j, end=" ")
        print("")
    # print(arr)

draw()

# 评分系统
def res():
    # 判断行
    for i in arr:
        str1 = ""
        for j in arr[arr.index(i)]:
            str1 += j
        if str1.find("●" * 5) > -1:
            print("恭喜你战胜了电脑")
            exit()
    # 判断列
    for i in range(size):
        str1 = ""
        for row in arr:
            str1 += row[i]
        if str1.find("●" * 5) > -1:
            print("恭喜你战胜了电脑")
            exit()
    # 判断对角
    for start in range(size):
        str1 = ""
        for i in arr:
            for j in i:
                str1 += j
        if str1[start::size + 1].find("●" * 5) > -1 or str1[start::size - 1].find("●" * 5) > -1:
            print("恭喜你战胜了电脑")
            exit()


while True:
    while True:
        print("用户下棋")
        str1 = input("请输入要落子的位置,格式如 1,1:\n")
        x, y = str1.split(",")
        x = int(x)
        y = int(y)
        print(arr[x][y])
        if x > 10 or y > 10:
            print("输入越界请重新输入")
            continue
        if arr[x][y] != "口":
            print("位置已落子，请重新选择位置")
            continue
        arr[x][y] = "●"
        draw()
        break
    while True:
        print("电脑下棋")
        x = randint(0, 9)
        y = randint(0, 9)
        print(x, y)
        if arr[x][y] != "口":
            continue
        if x >= 10 or y >= 10:
            continue
        arr[x][y] = "○"
        draw()
        break
    res()