
import turtle
import random

turtle.setup(width=600, height=600)  #調整視窗大小
turtle.colormode(255)
turtle.shape("turtle")  #調整烏龜外型 - 烏龜型
turtle.turtlesize(2,2)  #調整烏龜大小 - 參數為寬高為原來的幾倍
turtle.speed(5)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)


# 共9*9個方/ 每個方大小為90*90/ 間細為10/ 底盤大小為910*910
#畫在第一象限

turtle.pencolor(125,125,125)
turtle.fillcolor(125,125,125)

turtle.penup()
turtle.goto(0, 0)
turtle.setheading(0)
turtle.pendown()

turtle.begin_fill() #開始填色
turtle.forward(910)
turtle.left(90)
turtle.forward(910)
turtle.left(90)
turtle.forward(910)
turtle.left(90)
turtle.forward(910)
turtle.left(90)
turtle.end_fill()   #封閉圖形結束顏色

#n = 10
for i in range(1):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)

    turtle.penup()
    turtle.goto(10, 10)
    turtle.setheading(0)
    turtle.pendown()

    turtle.begin_fill()  # 開始填色
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.end_fill()  # 封閉圖形結束顏色


    # turtle.begin_fill() #開始填色
    # turtle.circle(200/n*(n+1-i))
    # turtle.end_fill()   #封閉圖形結束顏色


turtle.done()