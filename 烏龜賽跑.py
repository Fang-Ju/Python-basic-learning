
# required modules
import turtle
from turtle import *
from random import randint

# 視窗調整
w = 1400
h = 700
setup(w, h)

# classic shape turtle 控制內定(初始)的烏龜
speed(0)  # 初始的烏龜 速度
penup()   # 初始的烏龜 拿起筆
goto(-140, 140)  # 初始的烏龜 位置

# racing track 初始烏龜畫賽道
for step in range(15):
    write(step, align='center')  # turtle.write()在畫面上寫字 -> 中間對齊寫字 寫step迴圈變數 0 1 ... 13 14
    right(90) # 頭朝下

    for num in range(8):  # 畫虛線
        penup()
        forward(10)
        pendown()
        forward(10)

    penup()
    backward(160)  # 退回原位置
    left(90)       # 頭朝右
    forward(20)    # 移動20

# first player details 建立一個物件 第一個烏龜
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')

# first player proceeds to racing track
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()

# 360 degree turn
for turn in range(10):
    player_1.right(36)

# second player details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')

# second player enters in the racing track
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()

# 360 degree turn
for turn in range(72):
    player_2.left(5)

# third player details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')

# third player enters in the racing track
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()

# 360 degree turn
for turn in range(60):
    player_3.right(6)

# fourth player details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')

# fourth player enters in the racing track
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()

# 360 degree turn
for turn in range(30):
    player_4.left(12)

# turtles run at random speeds 賽跑
for turn in range(100): # 移動幾次 移動距離每隻烏龜隨機
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))


turtle.done()  # 不把動畫關掉