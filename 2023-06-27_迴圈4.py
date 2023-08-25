
import turtle
import random

turtle.setup(width=1400, height=600)  #調整視窗大小
turtle.colormode(255)
# turtle.shape("turtle")  #調整烏龜外型 - 烏龜型
# turtle.turtlesize(2,2)  #調整烏龜大小 - 參數為寬高為原來的幾倍
# turtle.speed(speed=0)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)


r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

turtle.pencolor(r,g,b)
turtle.fillcolor(r,g,b)

turtle.hideturtle()
turtle.tracer(0)  #畫圖的過程不顯示，呈現結果

x = -600  # x 初始位置
xd = 0.1  # 每一迴圈移動的距離
y = 200  # y 初始位置
yd = 0.1  # 每一迴圈移動的距離

while True :    #無窮迴圈
    turtle.clear()   #將烏龜畫的清除
    turtle.penup()
    turtle.goto(x, y) #放在正確的位置
    turtle.setheading(90)

    turtle.begin_fill()  # 開始填色
    # 畫一個方形
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.end_fill()  # 封閉圖形結束顏色

    turtle.update()  #將畫的圖案停留一下再進入下個迴圈清掉的動作

    if not -600 <= x <= 700: # x 如果方形要超出視窗(不再此範圍)
        xd = -xd  # 將移動距離正負相反
    x = x + xd  # 移動x軸距離

    if not -300 <= y <= 200: # y 如果方形要超出視窗(不再此範圍)
        yd = -yd  # 將移動距離正負相反
    y = y + yd  # 移動y軸距離


turtle.done()