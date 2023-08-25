# 5*5方陣，並隨機將其中任一方塊調色一點點，讓人猜猜哪個顏色不一樣的遊戲
import turtle
import random

turtle.setup(width=620, height=620)  #調整視窗大小
turtle.colormode(255)
turtle.shape("turtle")  #調整烏龜外型 - 烏龜型
turtle.turtlesize(2,2)  #調整烏龜大小 - 參數為寬高為原來的幾倍
turtle.speed(speed=0)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)


r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

turtle.pencolor(r,g,b)
turtle.fillcolor(r,g,b)

for j in range(5):  # row

    for i in range(5):   # col
        # 到方塊的左下角開始畫
        turtle.penup()
        turtle.goto(-190+i*120, 190-j*120)
        turtle.setheading(90)

        turtle.begin_fill()  # 開始填色
        # 畫一個方塊
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.end_fill()  # 封閉圖形結束顏色


turtle.hideturtle()  # 隱藏烏龜
x = random.randint(0, 4)  # 隨機挑選某一行
y = random.randint(0, 4)  # 隨機挑選某一列
# print(x)
# print(y)

# 顏色些微調整，並確認 r g b 參數不超過255
r = r + 50
if r > 255 :
    r = 255

g = g + 50
if g > 255 :
    g = 255

b = b + 50
if b > 255 :
    b = 255

turtle.pencolor(r,g,b)  # 改變畫筆顏色
turtle.fillcolor(r,g,b) # 改變填滿顏色

# 到隨機選擇的方形左下角位置
turtle.penup()
turtle.goto(-190+x*120, 190-y*120)
turtle.setheading(90)

turtle.begin_fill()  # 開始填色
# 畫一個方塊
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.end_fill()  # 封閉圖形結束顏色



turtle.done()