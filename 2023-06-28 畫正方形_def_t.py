import turtle as t
import random

def 畫正方形(x=0, y=0, size=100, r=0, g=0, b=0) :
    # 指定顏色
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

    # x,y 在方形的中間
    t.penup()
    t.goto(x,y)
    t.setheading(0)

    # 去左下角頭朝上
    t.fd(size/2)
    t.lt(90)
    t.bk(size/2)

    t.down()
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

    return None

t.setup(width=1400, height=600)  # 調整視窗大小
t.speed(speed=0)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)
t.colormode(255)
t.hideturtle()

畫正方形()  # 用預設值
畫正方形(650,250)  # 可以 -> x, y ，其他用預設值
畫正方形(size=100,r=0,g=0,b=255) # x,y用預設，其他用輸入值
畫正方形(650,-250,100,255,255,0)


t.done()