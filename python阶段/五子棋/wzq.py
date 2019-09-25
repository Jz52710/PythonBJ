from random import randint, choice

size = int(input("请输入棋盘大小:\n"))
arr = []

# 初始化棋盘
def init():
    for i in range(size):
        arr.append([])
        for j in range(size):
            arr[i].append("口")
init()

# 绘制棋盘
def draw():
    for i in arr:
        for j in arr[arr.index(i)]:
            print(j,end=" ")
        print("")
draw()


# 判断输赢

#五子棋游戏方法
# 绘制棋盘
# 落子（黑棋落子，白棋落子）
# 游戏规则（判断输赢）


