
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

for j in range(4):  # row

    for i in range(5):   # col
        turtle.penup()
        turtle.goto(-190+i*120, 190-j*120)
        turtle.setheading(90)

        turtle.begin_fill()  # 開始填色
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