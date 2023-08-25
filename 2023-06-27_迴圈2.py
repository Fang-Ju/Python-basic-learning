
import turtle
import random

turtle.setup(width=1200, height=600)  #調整視窗大小
turtle.colormode(255)
turtle.shape("turtle")  #調整烏龜外型 - 烏龜型
turtle.turtlesize(2,2)  #調整烏龜大小 - 參數為寬高為原來的幾倍
turtle.speed(5)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)

n = 10
for i in range(n):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)

    turtle.penup()
    turtle.goto(0,-200/n*(n+1-i))
    turtle.setheading(0)
    turtle.pendown()


    turtle.begin_fill() #開始填色
    turtle.circle(200/n*(n+1-i))
    turtle.end_fill()   #封閉圖形結束顏色

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
turtle.pencolor(r, g, b)

turtle.done()